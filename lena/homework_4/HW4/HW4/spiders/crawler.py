import scrapy


class OLXSpider(scrapy.Spider):
    name = "olx_el"
    start_urls = [
        'https://www.olx.ua/uk/elektronika/',
    ]

    def parse(self, response):
        l = []
        for link in response.css('div h3 a::attr(href)').extract():
            url = response.urljoin(link)
            l.append(url)
        for link_prod in l:
            yield scrapy.Request(link_prod, callback=self.parse2)



    def parse2(self, response):
        for info in response.css("div.offerdescription"):
            temp = info.css('li span::text').getall()
            c = False
            if '\n\t\t\t\tOLX Доставка\t\t\t' in temp:
                c = True
            inf = info.css('div[class="clr lheight20 large"]').get()


            yield {
                'product price': float(((info.css('div strong::text').get())[:-4]).replace(" ", "")),
                'product currency': ((info.css('div strong::text').get())[-4:]),
                'product name': (info.css('div h1::text').get())[9:-3],
                'product category': (info.css('a strong::text').getall())[1],
                'product photos urls': info.css('div img::attr(src)').get(default= ""),
                'product state': info.css('adress p::text').get(),
                'product description': inf,
                'product date of creation': info.css('em strong::text').get(),
                'product views count': info.css('span strong::text').get(),
                'product id': (info.css('li strong::text').getall())[-1],
                'olx delivery availability': c,
            }