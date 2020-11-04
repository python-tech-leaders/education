# Define here the models for your scraped items
#

import scrapy
from scrapy import Item, Field


class CategoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_price = Field()
    product_currency = Field()
    product_name = scrapy.Field()
    product_category = scrapy.Field()
    product_photos = scrapy.Field()
    product_description = scrapy.Field()
    product_id = scrapy.Field()
    product_date_of_creation = scrapy.Field()
    product_views_count = scrapy.Field()
    olx_delivery_availability = scrapy.Field()
    urls_product = scrapy.Field()
    state = scrapy.Field()
    seller_name = scrapy.Field()
    seller_address = scrapy.Field()
