import scrapy


class Product(scrapy.Item):
    price = scrapy.Field()
    name = scrapy.Field()
    category = scrapy.Field()
    photos_urls = scrapy.Field()
    state = scrapy.Field()
    description = scrapy.Field()
    date_of_creation = scrapy.Field()
    views_count = scrapy.Field()
    id = scrapy.Field()
    url = scrapy.Field()
    seller_name = scrapy.Field()
    seller_address = scrapy.Field()
    olx_delivery_availability = scrapy.Field()
