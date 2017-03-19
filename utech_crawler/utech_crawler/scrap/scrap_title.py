import urllib.request as req
import sys
from bs4 import BeautifulSoup
class ScrapTitle:

        def __init__(self,url):
                self.url = url
                res = req.urlopen(url)
                soup = BeautifulSoup(res, "html.parser")
                title_a = soup.find("title")
                title_w = str(title_a)
                title_t = title_w.replace("<title>","")
                title_b = title_t.replace(" - Qiita</title>","")
                self.title = title_b.replace(" ","")
        def output(self):
                return self.title
