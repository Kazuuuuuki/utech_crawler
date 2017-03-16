# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append("../scrap")
from scrap_condition import ScrapCondition
from scrap_links import ScrapLinks

class QiitaLikeSpider(scrapy.Spider):
    name = 'qiita_like'
    def start_requests(self):
        urls = [
            "http://qiita.com/tags/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92/likes"
        ]

        for url in urls:
            pages = 68
            for page in range(1, pages):
                new_url = url + "?page=" + str(page)
                scrap_links = ScrapCondition(new_url)
                for link in scrap_links.output():
                    yield scrapy.Request(url="http://qiita.com" + link, callback=self.parse)



    def parse(self, response):
        print(1)
        print(response.body)
        page = response.url.split("/")[-1]
        filename = '../articles/qiita-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        filename = "../articles/urls.txt"
        with open(filename, 'a') as f:
            f.write(response.url + ",")
        scrap_links = ScrapLinks(response.url)
        for url in scrap_links.output():
            yield scrapy.Request(url=url, callback=self.parse)
