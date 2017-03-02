# -*- coding: utf-8 -*-
import scrapy


class QiitaSpiderSpider(scrapy.Spider):
    name = "qiita_spider"


    def start_requests(self):
        urls = [
            'http://qiita.com/IshitaTakeshi/items/4607d9f729babd273960',
            'https://www.slideshare.net/yasutomo57jp/python-deep-learning?qid=23ef2196-84b6-40d7-918a-f9f4e7f83fdc&v=&b=&from_search=1'
        ]
        custome_setting = {
        'DOWNLOAD_DELAY': 10
        }
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = '../articles/qiita-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
