# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbListing(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    user_id = scrapy.Field()
    user_name = scrapy.Field()
    city = scrapy.Field()
    neighborhood = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    section_offset = scrapy.Field()
    bathrooms = scrapy.Field()
    bedrooms = scrapy.Field()
    beds = scrapy.Field()
    business_travel_ready = scrapy.Field()
    host_languages = scrapy.Field()
    new_listing = scrapy.Field()
    person_capacity = scrapy.Field()
    property_type = scrapy.Field()
    refundable = scrapy.Field()
    reviews_count = scrapy.Field()
    room_type = scrapy.Field()
    scrim_color = scrapy.Field()
    star_rating = scrapy.Field()
    superhost = scrapy.Field()
    tier_id = scrapy.Field()
    verified = scrapy.Field()
    price_rate = scrapy.Field()
    price_rate_type = scrapy.Field()
    weekly_price_factor = scrapy.Field()
    monthly_price_factor = scrapy.Field()
