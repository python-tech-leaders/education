import scrapy
from scrapy.exceptions import CloseSpider

from olx.items import OlxItem


class OlxSpider(scrapy.Spider):
    """
    olx spider for scraping data
    """

    # SETTINGS
    name = 'olx'
    start_urls = [
            'https://www.olx.ua/elektronika/'
        ]
    TARGET = 10
    count = 0
    # END

    # Catalog parser
    def parse(self, response):
        """
        Pagination parser for page with items
        """

        product_page_links = response.css('.detailsLink')
        yield from response.follow_all(product_page_links, self.parse_item)

        pagination_links = response.css('span.fleft a')
        yield from response.follow_all(pagination_links, self.parse)

    # Item Parser
    def parse_item(self, response):

        if OlxSpider.TARGET == OlxSpider.count:  # throw error when target ready
            raise CloseSpider('Exceeded maximum items')

        # Data cleaner
        cost = response.css('strong.pricelabel__value::text').get()
        price = cost[:cost.rfind(' ')]
        currency = cost[cost.rfind(' ') + 1:]

        params = (dict(zip(response.css('a.offer-details__param--url span::text').getall(),
                  response.css('a.offer-details__param--url strong::text').getall())))

        description = response.xpath('//div[@id="textContent"]//text()').extract()
        res_desc = ''
        for _str in description:
            _str = _str.strip().replace('\\n', ' ').replace('\\r', ' ').replace('\\t', ' ')
            res_desc += _str

        if response.css('ul#descGallery li a::attr(href)').getall():
            pics = response.css('ul#descGallery li a::attr(href)').getall()
        else:
            pics = response.css('div#descImage img::attr(src)')

        delivery = response.css('span.olx-delivery-badge-icon-wrapper').get()
        if delivery is not None:
            delivery = 'Есть Доставка OLX'
        else:
            delivery = 'Нет Доставка OLX'
        # end


        # Save Data
        item = OlxItem()
        item['product_url'] = response.url
        item['name'] = (response.css('div h1::text').get())[9:-3]
        item['category'] = response.css('td.middle ul li span::text').getall()
        item['price'] = float(price)
        item['price_currency'] = currency
        item['date_of_creation'] = response.css('em strong::text').get()
        item['count_views'] = int(response.css('span.offer-bottombar__counter strong::text').get())
        item['prod_id'] = response.css('ul.offer-bottombar__items li>strong::text').get()
        item['seller_name'] = response.css('div.offer-user__actions a::text').get().strip()
        item['seller_adress'] = response.css('address p::text').get()
        item['state'] = params.get('Состояние', 'Not Value')
        item['description'] = res_desc
        item['pics_urls'] = pics
        item['olx_delivery'] = delivery
        OlxSpider.count += 1
        # end

        yield item
