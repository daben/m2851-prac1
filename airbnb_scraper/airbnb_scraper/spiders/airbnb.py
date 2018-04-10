# -*- coding: utf-8 -*-
import scrapy
import json
import urllib
from airbnb_scraper.items import AirbnbListing


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['airbnb.com']
    default_currency = 'USD'
    price_range = (0, 1000, 10)
    page_limit = 20

    def __init__(self, query, currency=default_currency, **kwargs):
        super().__init__(**kwargs)
        self._place = query
        self._currency = currency
        self._api_path = "/api/v2/explore_tabs"
        self._api_key = None
        self._search_params = {}

    def start_requests(self):
        self.logger.info(f"starting survey for: {self._place}")
        yield self._api_request(callback=self.parse_landing_page)

    def parse_landing_page(self, response):
        data = self.read_data(response)
        self._search_params = self._get_search_params(data)
        self._neighborhoods = self._get_neighborhoods(data)

        tab = data['explore_tabs'][0]
        metadata = tab['home_tab_metadata']
        self._geography = metadata['geography']

        self.logger.info(f"Geography:\n{self._geography}")
        self.logger.info(f"Neighborhoods:\n{self._neighborhoods}")

        # Iterate area
        for neighborhood in self.iterate_neighborhoods(self._neighborhoods.values()):
            for price in self.iterate_prices(self.price_range):
                params = self._search_params.copy()
                params.update(neighborhood)
                params.update(price)
                yield self._api_request(params=params,
                                        response=response,
                                        callback=self.parse)

        # Parse the landing page in case something is missing
        for item in self.parse(response):
            yield item

    def iterate_neighborhoods(self, neighborhoods):
        for neighborhood in neighborhoods:
            yield {'neighborhood_ids[]': neighborhood['id']}

    def iterate_prices(self, price_range):
        # Iterate prices
        price_range_min, price_range_max, price_inc = price_range
        price_range_min = max(price_range_min, 0)
        price_range_max = max(price_range_max, price_range_min + price_inc)

        for price_min in range(price_range_min, price_range_max, price_inc):
            price_max = price_min + price_inc
            params = {}
            if price_min > price_range_min:
                params['price_min'] = price_min
            if price_max < price_range_max:
                params['price_max'] = price_max
            yield params

    def parse(self, response):
        data = self.read_data(response)

        tab = data['explore_tabs'][0]
        pagination = tab['pagination_metadata']
        section_offset = pagination['section_offset']

        # Handle pagination
        if section_offset < self.page_limit:
            listings = tab['sections'][0]['listings']

            if pagination['has_next_page']:
                next_section = self._search_params.copy()
                next_section.update({
                    'section_offset': section_offset + 1,
                    'items_offset': (section_offset + 1) * len(listings)
                })
                yield self._api_request(params=next_section,
                                        response=response)

        for item in self.parse_listings(data):
            yield item

    def parse_listings(self, data):
        if isinstance(data, scrapy.http.Response):
            data = self.read_data(data)

        tab = data['explore_tabs'][0]
        pagination = tab['pagination_metadata']
        section_offset = pagination['section_offset']
        listings = tab['sections'][0]['listings']
        self.logger.info(f"num listings: {len(listings)}")

        for item in listings:
            x = item['listing']
            q = item['pricing_quote']
            yield AirbnbListing(
                _id=x["id"],
                name=x["name"].replace("\n", " -- "),
                user_id=x['user']['id'],
                user_name=x['user']['first_name'],
                section_offset=section_offset,
                neighborhood=x['neighborhood'],
                city=x['city'],
                latitude=x['lat'],
                longitude=x['lng'],
                bathrooms=x['bathrooms'],
                bedrooms=x['bedrooms'],
                beds=x['beds'],
                business_travel_ready=x['is_business_travel_ready'],
                host_languages=x['host_languages'],
                new_listing=x['is_new_listing'],
                person_capacity=x['person_capacity'],
                property_type=x['property_type_id'],
                refundable=x['is_fully_refundable'],
                reviews_count=x['reviews_count'],
                room_type=x['room_type_category'],
                scrim_color=x['scrim_color'],
                star_rating=x['star_rating'],
                superhost=x['is_superhost'],
                tier_id=x['tier_id'],
                verified=item['verified_card'],
                price_rate=q['rate']['amount'],
                price_rate_type=q['rate_type'],
                weekly_price_factor=q['weekly_price_factor'],
                monthly_price_factor=q['monthly_price_factor']
            )

    def _get_neighborhoods(self, data):
        meta = data['explore_tabs'][0]['home_tab_metadata']
        facets = meta['facets']['neighborhood_facet']

        neighborhoods = {}
        for item in facets:
            neighborhoods[item['key']] = item

        for section in meta['filters']['sections']:
            if section['filter_section_id'] == 'neighborhoods':
                for item in section['items']:
                    key = item['title']
                    for param in item['params']:
                        if param['key'] == 'neighborhood_ids':
                            neighborhoods[key]['id'] = param['value']
                            break

        return neighborhoods

    def _get_search_params(self, data):
        tab = data['explore_tabs'][0]
        pagination = tab['pagination_metadata']

        metadata = tab['home_tab_metadata']
        geography = metadata['geography']
        location = metadata['location']

        params = {
            'federated_search_session_id':
                data['metadata']['federated_search_session_id'],
            'last_search_session_id':
                pagination['search_session_id'],
            'place_id':
                geography['place_id'],
            'query':
                location['canonical_location']
        }
        return params

    def read_data(self, response):
        self.logger.debug(f"Parsing {response.url}")
        data = json.loads(response.body)
        return data

    def _api_request(self, params=None, response=None, callback=None):
        if response:
            request = response.follow
        else:
            request = scrapy.Request

        callback = callback or self.parse

        return request(self._api_url(params), callback)

    def _api_url(self, params=None):
        if self._api_key is None:
            self._api_key = self.settings.get("AIRBNB_API_KEY")

        query = {
            'version': '1.3.5',
            '_format': 'for_explore_search_web',
            'items_per_grid': '50',
            'experiences_per_grid': '20',
            'guidebooks_per_grid': '20',
            'auto_ib': 'false',
            'fetch_filters': 'true',
            'has_zero_guest_treatment': 'false',
            'is_guided_search': 'true',
            'is_new_cards_experiment': 'true',
            'luxury_pre_launch': 'false',
            'query_understanding_enabled': 'true',
            'show_groupings': 'true',
            'supports_for_you_v3': 'true',
            'timezone_offset': '',
            'metadata_only': 'false',
            'is_standard_search': 'true',
            'tab_id': 'home_tab',
            # 'section_offset': '0',
            # 'items_offset': '0',
            'recommendation_item_cursor': '',
            'refinement_paths[]': '/homes',
            # 'place_id': '',
            # 'last_search_session_id': '',
            # 'federated_search_session_id': '',
            # 'ne_lat': ,
            # 'ne_lng': ,
            # 'sw_lat': ,
            # 'sw_lng': ,
            # 'zoom': 14,
            # 'price_min': 10,
            # 'price_max': None,
            # 'neighborhood_ids[]': ,
            'screen_size': 'medium',
            'query': self._place,
            '_intents': 'p1',
            'key': self._api_key,
            'currency': self._currency,
            'locale': 'en'}

        if params:
            query.update(params)
        return self._build_airbnb_url(self._api_path, query)

    def _build_airbnb_url(self, path, query=None):
        if query is not None:
            query = urllib.parse.urlencode(query)
        parts = ['https', 'www.airbnb.com', path, None, query, None]
        return urllib.parse.urlunparse(parts)
