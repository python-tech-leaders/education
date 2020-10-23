import scrapy

from olx.items import OlxItem


class OlxSpider(scrapy.Spider):
    name = 'olx'
    start_urls = [
            'https://www.olx.ua/elektronika/'
        ]

    def parse(self, response):
        items = response.css('table#offers_table a.detailsLink::attr(href)').getall()
        pagination = response.css("span.fleft a::attr(href)").getall()
        page_status = response.css("span.fleft span::attr(class)").getall()
        urls_res = [url for url in set(items) if
                    url.find('https://www.olx.ua/obyavlenie/') != -1]

        with open(file='log.txt', mode='a', encoding='utf8') as file:
            file.write(str(page_status))
        while len(pagination):
            while urls_res:
                url = urls_res.pop()
                yield scrapy.Request(url=url, callback=self.parse_item)
            url_p = pagination.pop()

            yield scrapy.Request(url=url_p, callback=self.parse)

    def parse_item(self, response):

        cost = response.css('strong.pricelabel__value::text').get()
        price = cost[:cost.rfind(' ')]
        currency = cost[cost.rfind(' ') + 1:]
        params = (dict(zip(response.css('a.offer-details__param--url span::text').getall(),
                  response.css('a.offer-details__param--url strong::text').getall())))
        delivery = response.css('span.olx-delivery-badge-icon-wrapper').get()
        if delivery is not None:
            delivery = 'Есть Доставка OLX'
        else:
            delivery = 'Нет Доставка OLX'
        description = response.xpath('//div[@id="textContent"]//text()').extract()
        res_desc = ''
        for _str in description:
            _str = _str.strip().replace('\\n', ' ').replace('\\r', ' ').replace('\\t', ' ')
            res_desc += _str

        item = OlxItem()
        item['product_url'] = response.url
        item['name'] = (response.css('div h1::text').get())[9:-3]
        item['category'] = response.css('td.middle ul li span::text').getall()
        item['price'] = price
        item['price_currency'] = currency
        item['date_of_creation'] = response.css('em strong::text').get()
        item['count_views'] = response.css('span.offer-bottombar__counter strong::text').get()
        item['prod_id'] = response.css('ul.offer-bottombar__items li>strong::text').get()
        item['seller__name'] = response.css('div.offer-user__actions a::text').get().strip()
        item['seller_adress'] = response.css('address p::text').get()
        item['state'] = params.get('Состояние', 'Итак сойдет')
        item['description'] = res_desc
        item['pics_urls'] = response.css('ul#descGallery li a::attr(href)').getall()
        item['olx_delivery'] = delivery

        yield item
