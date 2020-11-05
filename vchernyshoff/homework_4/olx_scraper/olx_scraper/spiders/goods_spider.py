import scrapy
from scrapy.exceptions import CloseSpider

# https://www.olx.ua/elektronika/?page=2

# from items import OlxScraperItem
from ..items import OlxScraperItem


class GoodSpider(scrapy.Spider):
    name = 'goods'
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
            good = OlxScraperItem()
            good['name'] = extract_with_css('h1::text')
            good['url'] = response.url
            good['price'] = int(''.join(response.css(
                '.not-arranged::text')[0].re(r'\d')))
            good['currency'] = ''.join(response.css(
                '.not-arranged::text')[0].re(r'\D')).strip()
            good['category'] = response.css(
                'td.middle span::text').getall()
            good['state'] = response.css(
                'strong.offer-details__value::text').re(r'Новый|Б/у')[0]
            good['description'] = extract_with_css('#textContent::text')
            good['date_of_creation'] = extract_with_css('em strong::text')
            good['views_count'] = int(extract_with_css(
                '.offer-bottombar__counter strong::text'))
            good['id'] = extract_with_css(
                '.offer-bottombar__item~ .offer-bottombar__item+ .offer-bottombar__item strong::text')
            good['photos_urls'] = response.css(
                '#descGallery li a::attr(href)').getall()
            good['seller_name'] = extract_with_css('h4 a::text')
            good['seller_address'] = response.xpath(
                '//*[@id="offeractions"]/div[4]/div[2]/div[1]/address/p/text()').get()
            good['olx_delivery_availability'] = extract_with_css(
                '.AdPageBox__link-button-caption::text')
            self.count += 1

            yield good
        else:
            raise CloseSpider('Exceeded maximum items')
            
