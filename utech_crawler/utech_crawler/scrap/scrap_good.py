import urllib.request as req
import sys
from bs4 import BeautifulSoup

class ScrapGood:

    def __init__(self,url):
        self.url = url
        res = req.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        good = []
        link = []
        self.select_link = []
        good_list = soup.find_all("ul" , class_="ItemLink__status")
        link_list = soup.select(".media > div.media__body > div.ItemLink__title > a")
        for a in link_list:
            link.append(a.attrs['href'])
        for num in range(len(link_list)):
            ward = str([good_list[num]])
            good_list[num].span.decompose()
            if "fa-comment-o" in ward:
                good_list[num].a.decompose()
                good.append(good_list[num].text)
            else:
                good.append(good_list[num].text)
            dict_link = {good[num]:link[num]}
            number = int(good[num])
            if number > 100:
                self.select_link.append(dict_link[good[num]])
    def output(self):
        return self.select_link
