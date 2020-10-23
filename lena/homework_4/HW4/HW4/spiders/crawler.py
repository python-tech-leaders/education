import scrapy
from .. items import tem
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
        l = []
        for link in response.css('div h3 a::attr(href)').extract():
            url = response.urljoin(link)
            l.append(url)
        for link_prod in l:
            yield scrapy.Request(link_prod, callback=self.parse0)
        pagination_links = response.css('span.fleft a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse0(self, response):
        if self.count<100:
            for info in response.css("div.offerdescription"):
                product_price = info.css('div strong::text').get()
                product_name = (info.css('div h1::text').get())[9:-3]
                product_category = (info.css('a strong::text').getall())[1]
                product_photos = info.css('div img::attr(src)').get(default= "")
                product_description = info.css('#textContent::text').get(default='').strip()
                product_id = info.css('.offer-bottombar__item~ .offer-bottombar__item+ .offer-bottombar__item strong::text').get(default='').strip()
                produc_date_of_creation = info.css('em strong::text').get()
                product_views_count = info.css('span strong::text').get()
                olx_delivery_availability = info.css('.AdPageBox__link-button-caption::text').get(default='').strip()
                urls_product = info.xpath('/html/head/link[1]/@href').get()
                seller_name = info.css('h4 a::text').get(default = '').strip()
                seller_address = info.xpath('//*[@id="offeractions"]/div[4]/div[2]/div[1]/address/p/text()').get()

                product = tem()

                product['product_price'] = product_price
                product['product_name'] = product_name
                product['product_category'] = product_category
                product['product_photos'] = product_photos
                product['product_description'] = product_description
                product['product_id'] = product_id
                product['produc_date_of_creation'] = produc_date_of_creation
                product['product_views_count'] = product_views_count
                product['olx_delivery_availability'] = olx_delivery_availability
                product['urls_product'] = urls_product
                product['seller_name'] = seller_name
                product['seller_address'] = seller_address


                self.count += 1
                print(self.count)
                yield product
                if self.count == 100:
                    raise CloseSpider()
