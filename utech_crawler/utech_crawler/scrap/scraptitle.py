import urllib.request as req
import sys
from bs4 import BeautifulSoup
class ScrapTitle:

        def __init__(self,url):
                self.url = url
                res = req.urlopen(url)
                soup = BeautifulSoup(res, "html.parser")
                self.title = soup.find("title")
        def output(self):
                print (self.title.string)
