
# Bali Airbnb April 2018
## A look to the Airbnb property listings in Bali, Indonesia

![A view of Bali][ref:image]
<span style="font-size: 8pt; float:right;">
  Image: CC BY SA-3.0 &mdash; *[A view of Bali][ref:image_source]*
</span>

### Author

David Moriano <[dmoriano@uoc.edu](mailto:dmoriano@uoc.edu)>

### Context

Airbnb claims to be part of the "sharing economy" and disrupting the hotel industry. By analyzing the data for a city or region we can see for ourselves the actual impact of "home sharing".

### Content

The dataset contains +12,000 property listings from Bali, Indonesia collected on April, 2018. This is not a complete collection of all the listings available but hopefully a good representation.

The data has been scraped from airbnb.com with a custom web scraper built with [Scrapy][ref:scrapy]. The crawler iterates on the Bali neighborhoods as provided by Airbnb and on the price range.

Note that the scraper is generic enough to work on other cities, but this hasn't been tested.

Also note that the scraper would stop working if Airbnb makes any changes in their API or scraping policies.

The dataset includes the following columns:

| Column | Description | Type |
| ------ | ----------- | ---- |
| _id | Listing identifier in Airbnb | Numeric |
| name | Name of the listing | String |
| user_id | User identifier of the host | Numeric |
| user_name | First name of the host | String |
| city | City name | String |
| neighborhood | Neighborhood | String |
| latitude | Latitude of the neighborhood | Numeric |
| longitude | Longitude of the neighborhood | Numeric |
| section_offset | Page number on which it was listed | Numeric |
| bathrooms | Number of bathrooms | Numeric |
| bedrooms | Number of bedrooms | Numeric |
| beds | Number of beds | Numeric |
| business_travel_ready | Can accommodate business travelers | Boolean |
| host_languages | Host languages | Array |
| new_listing | Is it a new listing? | Boolean |
| person_capacity | Guests capacity | Numeric |
| property_type | Type of property | Numeric |
| refundable | Is it refundable | Boolean |
| reviews_count | Number of review | Numeric |
| room_type | Room type | Numeric |
| scrim_color | [Scrim][ref:scrim] color | String |
| star_rating | Star rating given by the guests | Numeric |
| superhost | Is the host a superhost | Boolean |
| tier_id | Tier identifier | Numeric |
| verified | Is it a verified host | Boolean |
| price_rate | Price rate in USD | Numeric |
| price_rate_type | Price rate type | Numeric |
| weekly_price_factor | Weekly stay discount factor | Numeric |
| monthly_price_factor | Monthly stay discount factor | Numeric |

### Inspiration - What can you do with this data?

You could use this dataset to find your ideal airbnb hosting in your next holidays in Bali (or any other city you scrap). Or maybe, you are an Airbnb host and you want to know what is the ideal price for your property. These are all useful and practical questions, but we can look a little bigger.

The interest in Airbnb data rises after Murray Cox's research ([InsideAirbnb.com][ref:insideairbnb]) on the impact of Airbnb on the [gentrification][ref:gentrification] of New York. He is trying to answer some relevant questions given the size of Airbnb: How is Airbnb really being used, and how is it affecting the neighborhoods of New York City. His research has been recently expanded by the Urban Planning and Governance research group at McGill University. They just published a [report][ref:upgo-report] to answer these questions:

1. Where is Airbnb activity located in New York, and how is it changing?
2. Who makes money from Airbnb in New York?
3. How much housing has Airbnb removed from the market in New York?
4. Is Airbnb driving gentrification in New York?

Also, the [CityLab][ref:citylab] magazine has published an interesting [article][ref:citylab-article] about this research.

Yet one could ask the same questions about other cities.

Why Bali? Well, Bali is considered the cultural center in Indonesia, and it's also one the most touristic spots in the planet. Given that tourism makes up 80% of its economy, and that Airbnb has a significant activity in the island, it's natural to wonder what's happening. And this dataset, being just a shot in time, won't be enough to answer all these questions, but it surely can be a start point.

### License

This dataset is released under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc:by-nc].

This means you are free to:

- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following terms:

- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

- NonCommercial — You may not use the material for commercial purposes.

The full details of the [license][cc:by-nc-legalcode] can be found in the previous link.

### Acknowledgment

Thanks to Airbnb for allowing the scraping of their website. And thanks to the [Scrapy][ref:scrapy] developers for a wonderful framework.

### Code

The source code of the scraper is in the `airbnb_scraper` folder. It's licensed under the [MIT License](airbnb_scraper/LICENSE).

To run again the crawler you can do:
```bash
$ scrapy crawl airbnb -a query="Bali, Indonesia" -o bali_listings.csv
```

### Files

| File | Description |
|:-----|:------------|
| .gitignore | Specifies intentionally untracked files to ignore in the repository |
| Pipfile | See https://github.com/pypa/pipenv |
| Pipfile.lock | ditto |
| README.md | This document |
| airbnb_scraper/ | Scraper code |
| airbnb_scraper/LICENSE | Code License |
| airbnb_scraper/airbnb_scraper/__init__.py | Module initialization |
| airbnb_scraper/airbnb_scraper/items.py | AirbnbListing item |
| airbnb_scraper/airbnb_scraper/middlewares.py | Middleware (not used) |
| airbnb_scraper/airbnb_scraper/pipelines.py | Pipelines: remove duplicates |
| airbnb_scraper/airbnb_scraper/settings.py | Scraper settings |
| airbnb_scraper/airbnb_scraper/spiders/__init__.py | Spiders module |
| airbnb_scraper/airbnb_scraper/spiders/airbnb.py | Airbnb spider |
| airbnb_scraper/scrapy.cfg | Scrapy configuration file |
| assets/banner.jpg | Banner image |
| data/listings_bali_201804.csv | Dataset in CSV |

### Dataset

- [listings_bali_201804.csv][ref:dataset] (~3MiB)


[//]: # (References)

[ref:image]: ./assets/banner.jpg
[ref:image_source]: https://commons.wikimedia.org/wiki/Bali#/media/File:Ubud_banner.jpg
[ref:scrapy]: https://scrapy.org/
[ref:scrim]: https://en.wikipedia.org/wiki/Scrim_(lighting)
[ref:insideairbnb]: http://insideairbnb.com/index.html
[ref:gentrification]: https://en.wikipedia.org/wiki/Gentrification
[ref:citylab]: https://www.citylab.com/
[ref:citylab-article]: https://www.citylab.com/equity/2018/03/what-airbnb-did-to-new-york-city/552749/
[ref:upgo-report]: https://mcgill.ca/newsroom/files/newsroom/channels/attach/airbnb-report.pdf
[ref:dataset]: ./data/listings_bali_201804.csv
[cc:by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc:by-nc-legalcode]: https://creativecommons.org/licenses/by-nc/4.0/legalcode
