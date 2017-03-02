import urllib.request as req
import sys
from bs4 import BeautifulSoup
class Scraplinks:

        def __init__(self,url):
                self.url = url
                res = req.urlopen(url)
                soup = BeautifulSoup(res, "html.parser")
                links_list = soup.select('a[href^="http://qiita"]')
                for a in links_list:
                        self.href = a.attrs['href']
        def output(self):
                print(self.href)
