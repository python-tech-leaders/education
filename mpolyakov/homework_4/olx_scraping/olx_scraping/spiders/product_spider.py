import scrapy
from scrapy.item import Item, Field


class Product(Item):
    name = Field()
    price = Field()
    category = Field()
    state = Field()
    description = Field()
    date_of_creation = Field()
    views_count = Field()
    pid = Field()
    seller_name = Field()
    olx_delivery_availability = Field()


class ProductSpider(scrapy.Spider):
    name = 'products'

    custom_settings = {
        'FEED_URI': 'output.json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEED_EXPORT_INDENT': 4,
        'CLOSESPIDER_ITEMCOUNT': 2,
        # 'CLOSESPIDER_PAGECOUNT': 2,
        # 'CONCURRENT_REQUESTS': 2,
    }

    allowed_domains = ['olx.ua']
    start_urls = [
        'https://www.olx.ua/elektronika/',
        # 'https://www.olx.ua/elektronika/?page=2',
        # 'https://www.olx.ua/elektronika/?page=3',
    ]

    def parse(self, response):
        product_page_links = response.css('.detailsLink')
        yield from response.follow_all(product_page_links, self.parse_product)

    def parse_product(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        product = Product()
        product['name'] = extract_with_css('h1::text')
        product['price'] = extract_with_css('.not-arranged::text')
        product['category'] = response.css(
            'strong.offer-details__value::text')[1].get()
        product['state'] = response.css(
            'strong.offer-details__value::text').re(r'Новый|Б/у')
        product['description'] = extract_with_css('#textContent::text')
        product['date_of_creation'] = extract_with_css('em strong::text')
        product['views_count'] = extract_with_css(
            '.offer-bottombar__counter strong::text')
        product['pid'] = extract_with_css(
            '.offer-bottombar__item~ .offer-bottombar__item+ .offer-bottombar__item strong::text')
        product['seller_name'] = extract_with_css('h4 a::text')
        product['olx_delivery_availability'] = extract_with_css(
            '.AdPageBox__link-button-caption::text')

        yield product


'''
product photos urls !!!
product url !!!
seller address !!!
'''
'''
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 100,
        'CONCURRENT_REQUESTS': 100,
        'CLOSESPIDER_ITEMCOUNT': 100,
    }
'''
