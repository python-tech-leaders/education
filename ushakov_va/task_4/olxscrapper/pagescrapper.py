import scrapy
from datetime import datetime

from .item import Product

_months = {
    'января': 'Jan',
    'февраля': 'Feb',
    'марта': 'Mar',
    'арпеля': 'Apr',
    'мая': 'May',
    'июня': 'June',
    'июля': 'Jul',
    'августа': 'Aug',
    'сентября': 'Sept',
    'октября': 'Oct',
    'ноября': 'Nov',
    'декабря': 'Dec'
}


def _multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


class ElectronicsSpider(scrapy.Spider):
    def __init__(self, count_row=100, **kwargs):
        super().__init__(**kwargs)
        self.count_row = count_row
        self.count_now = 0

    name = 'electronics'
    allowed_domains = ['olx.ua']

    def check_count(func):
        def _decor(self, response):
            if self.count_now >= self.count_row:
                return
            try:
                result = func(self, response)
                self.count_now += 1
                return result
            except:
                return

        return _decor

    def start_requests(self):
        i = 0
        while self.count_row > self.count_now:
            if i * 44 < self.count_row:
                i += 1
                yield scrapy.Request(f'https://www.olx.ua/elektronika/?page={i}', callback=self.parse)
            else:
                return

    def parse(self, response):
        # print(len(response.xpath('//h3[@class="lheight22 margintop5"]/a/@href').extract()))
        for link in response.xpath('//h3[@class="lheight22 margintop5"]/a/@href').extract():
            absoluteLink = response.urljoin(link)
            yield scrapy.Request(url=absoluteLink, callback=self.parse_item)

    @check_count
    def parse_item(self, response):
        item = Product()
        item['price'] = response.xpath("//div[@class='pricelabel']/strong/text()")[0].get().strip()
        item['name'] = response.xpath("//div[@class='offer-titlebox']/h1/text()").get().strip()
        item['category'] = response.xpath(
            "//li[@class='offer-details__item'][2]/a[@class='offer-details__param offer-details__param--url']/strong[@class='offer-details__value']/text()").get().strip()
        item['photos_urls'] = [i.get() for i in response.xpath("//li[@class='fleft']/a/@href")]
        item['state'] = (
                [i for i in response.xpath("//strong[@class='offer-details__value']/text()") if i.root == 'Б/у'] +
                [i for i in response.xpath("//strong[@class='offer-details__value']/text()") if i.root == 'Новый'])[
            0].get()
        item['description'] = ''.join([i.get().strip() for i in response.xpath("//div[@id='textContent']/text()")])
        text_of_date_of_creation = response.xpath(
            "//li[@class='offer-bottombar__item'][1]/em/strong/text()").get().strip()  # get text from site
        text_of_date_of_creation = _multiple_replace(text_of_date_of_creation,
                                                     _months)  # change month's name from Russian to English
        item['date_of_creation'] = datetime.strptime(text_of_date_of_creation, 'в %H:%M, %d %b %Y').strftime(
            "%Y-%m-%d-%H.%M.%S")  # convert to correct datetime format
        item['views_count'] = response.xpath(
            "//li[@class='offer-bottombar__item'][2]/span[@class='offer-bottombar__counter']/strong/text()").get().strip()
        item['id'] = response.xpath("//li[@class='offer-bottombar__item'][3]/strong/text()").get().strip()
        item['url'] = response.url.strip()
        item['seller_name'] = response.xpath("//div[@class='offer-user__actions']/h4/a/text()").get().strip()
        item['seller_address'] = response.xpath("//div[@class='offer-user__address']/address/p/text()").get().strip()
        item['olx_delivery_availability'] = True if len(
            response.xpath("//span[@class=' AdPageBox__link-button-caption  svelte-14f8vge']")) > 0 else False

        return item
