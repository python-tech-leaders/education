# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxItem(scrapy.Item):
    price = scrapy.Field()
    price_currency = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    pics_urls = scrapy.Field()
    state = scrapy.Field()
    description = scrapy.Field()
    date_of_creation = scrapy.Field()
    count_views = scrapy.Field()
    prod_id = scrapy.Field()
    product_url = scrapy.Field()
    seller__name = scrapy.Field()
    seller_adress = scrapy.Field()
    olx_delivery = scrapy.Field()
