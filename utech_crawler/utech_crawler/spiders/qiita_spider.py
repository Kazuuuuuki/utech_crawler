# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append("../scrap")
from scrap_links import ScrapLinks

class QiitaSpiderSpider(scrapy.Spider):
    name = "qiita_spider"


    def start_requests(self):
        urls = [
            "http://qiita.com/7shi/items/145f1234f8ec2af923ef"
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = '../articles/qiita-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        scrap_links = ScrapLinks(response.url)
        for url in scrap_links.output():
            yield scrapy.Request(url=url, callback=self.parse)
