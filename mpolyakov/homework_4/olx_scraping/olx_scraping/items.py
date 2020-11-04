# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item


class Product(Item):
    name = Field()
    url = Field()
    price = Field()
    currency = Field()
    category = Field()
    state = Field()
    description = Field()
    date_of_creation = Field()
    views_count = Field()
    id = Field()
    photos_urls = Field()
    seller_name = Field()
    seller_address = Field()
    olx_delivery_availability = Field()
