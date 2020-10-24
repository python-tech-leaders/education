import scrapy
from datetime import datetime

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
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str


class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    allowed_domains = ['olx.ua']
    start_urls = ['https://www.olx.ua/obyavlenie/perehodnik-dlya-naushnikov-lightning-3-5-mm-original-apple-aux-mini-jac-IDJ6iia.html#c9051cd4d2']


    def parse(self, response):
        item = Product()
        item['price'] = response.xpath("//div[@class='pricelabel']/strong/text()")[0].get().strip()
        item['name'] = response.xpath("//div[@class='offer-titlebox']/h1/text()").get().strip()
        item['category'] = response.xpath("//li[@class='offer-details__item'][2]/a[@class='offer-details__param offer-details__param--url']/strong[@class='offer-details__value']/text()").get().strip()
        item['photos_urls'] = [i.get() for i in response.xpath("//li[@class='fleft']/a/@href")]
        item['state'] = ([i for i in response.xpath("//strong[@class='offer-details__value']/text()") if i.root == 'Б/у'] + [i for i in response.xpath("//strong[@class='offer-details__value']/text()") if i.root == 'Новый'])[0].get()
        item['description'] = ''.join([i.get().strip() for i in response.xpath("//div[@id='textContent']/text()")])
        item['date_of_creation'] = datetime.strptime(_multiple_replace(response.xpath("//li[@class='offer-bottombar__item'][1]/em/strong/text()").get().strip(), _months), 'в %H:%M, %d %b %Y').strftime("%Y-%m-%d-%H.%M.%S")
        item['views_count'] = response.xpath("//li[@class='offer-bottombar__item'][2]/span[@class='offer-bottombar__counter']/strong/text()").get().strip()
        item['id'] = response.xpath("//li[@class='offer-bottombar__item'][3]/strong/text()").get().strip()
        item['url'] = response.url.strip()
        item['seller_name'] = response.xpath("//div[@class='offer-user__actions']/h4/a/text()").get().strip()
        item['seller_address'] = response.xpath("//div[@class='offer-user__address']/address/p/text()").get().strip()
        item['olx_delivery_availability'] = True if len(response.xpath("//span[@class=' AdPageBox__link-button-caption  svelte-14f8vge']")) > 0 else False

        return item