# -*- coding: utf-8 -*-
import scrapy


class QiitaSpiderSpider(scrapy.Spider):
    name = "qiita_spider"


    def start_requests(self):
        urls = [
            'http://qiita.com/IshitaTakeshi/items/4607d9f729babd273960',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
