import scrapy
from scrapy.exceptions import CloseSpider

from olx_scraping.items import Product


class ProductSpider(scrapy.Spider):
    name = 'products'

    custom_settings = {
        'FEED_URI': 'output.json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CLOSESPIDER_ITEMCOUNT': 10,
    }

    allowed_domains = ['olx.ua']
    start_urls = ['https://www.olx.ua/elektronika/']

    MAX_COUNT = 10  # defines maximum items to store
    count = 0

    def parse(self, response):
        """
        Find links to product page.
        """
        product_page_links = response.css('.detailsLink')
        yield from response.follow_all(product_page_links, self.parse_product)

        pagination_links = response.css('span.fleft a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_product(self, response):
        """
        Extract data from product page
        """
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        if self.count < self.MAX_COUNT:
            product = Product()
            product['name'] = extract_with_css('h1::text')
            product['url'] = response.url
            product['price'] = int(''.join(response.css(
                '.not-arranged::text')[0].re(r'\d')))
            product['currency'] = ''.join(response.css(
                '.not-arranged::text')[0].re(r'\D')).strip()
            product['category'] = response.css(
                'td.middle span::text').getall()
            product['state'] = response.css(
                'strong.offer-details__value::text').re(r'Новый|Б/у')[0]
            product['description'] = extract_with_css('#textContent::text')
            product['date_of_creation'] = extract_with_css('em strong::text')
            product['views_count'] = int(extract_with_css(
                '.offer-bottombar__counter strong::text'))
            product['id'] = extract_with_css(
                '.offer-bottombar__item~ .offer-bottombar__item+ .offer-bottombar__item strong::text')
            product['photos_urls'] = response.css(
                '#descGallery li a::attr(href)').getall()
            product['seller_name'] = extract_with_css('h4 a::text')
            product['seller_address'] = response.xpath(
                '//*[@id="offeractions"]/div[4]/div[2]/div[1]/address/p/text()').get()
            product['olx_delivery_availability'] = extract_with_css(
                '.AdPageBox__link-button-caption::text')
            self.count += 1

            yield product
        else:
            raise CloseSpider('Exceeded maximum items')
