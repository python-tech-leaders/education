import scrapy
from .. items import CategoryItem
from scrapy.exceptions import CloseSpider

class OLXSpider(scrapy.Spider):
    name = "olx_el"
    allowed_domains = ['olx.ua']
    start_urls = [
        'https://www.olx.ua/uk/elektronika/',
    ]
    custom_settings = {
        'FEED_URI': 'output.json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CLOSESPIDER_ITEMCOUNT': 100,
    }

    count = 0

    def parse(self, response):
        for link in response.css('div h3 a::attr(href)').extract():
            url = response.urljoin(link)
            yield scrapy.Request(url, callback=self.parse_website)
        pagination_links = response.css('span.fleft a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_website(self, response):
        if self.count<100:

            product_price = int(''.join(response.css('.not-arranged::text')[0].re(r'\d')))
            product_currency = ''.join(response.css('.not-arranged::text')[0].re(r'\D')).strip()
            product_name = (response.css('div h1::text').get())[9:-3]
            product_category = (response.css('a strong::text').getall())[1]
            product_photos = response.css('#descGallery li a::attr(href)').getall()
            product_description = response.css('#textContent::text').get(default='').strip()
            product_id = response.css('.offer-bottombar__item~ .offer-bottombar__item+ .offer-bottombar__item strong::text').get(default='').strip()
            product_date_of_creation = response.css('em strong::text').get()
            product_views_count = int(response.css('.offer-bottombar__counter strong::text').get(default = '').strip())
            olx_delivery_availability = response.css('.AdPageBox__link-button-caption::text').get(default = '').strip()
            urls_product = response.xpath('/html/head/link[1]/@href').get()
            seller_name = response.css('h4 a::text').get(default = '').strip()
            seller_address = response.xpath('//*[@id="offeractions"]/div[4]/div[2]/div[1]/address/p/text()').get(default = '')

            product = CategoryItem()

            product['product_price'] = product_price
            product['product_currency'] = product_currency
            product['product_name'] = product_name
            product['product_category'] = product_category
            product['product_photos'] = product_photos
            product['product_description'] = product_description
            product['product_id'] = product_id
            product['product_date_of_creation'] = product_date_of_creation
            product['product_views_count'] = product_views_count
            product['olx_delivery_availability'] = olx_delivery_availability
            product['urls_product'] = urls_product
            product['seller_name'] = seller_name
            product['seller_address'] = seller_address


            self.count += 1
            print(self.count)
            yield product
        else:
            raise CloseSpider()
