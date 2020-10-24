from scrapy.crawler import CrawlerProcess
from scrapy import signals
from scrapy.signalmanager import dispatcher

import olxscrapper

if __name__ == '__main__':
    results = []


    def crawler_results(signal, sender, item, response, spider):
        results.append(item)


    dispatcher.connect(crawler_results, signal=signals.item_passed)
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(olxscrapper.ElectronicsSpider)
    process.start()
    print(results)
