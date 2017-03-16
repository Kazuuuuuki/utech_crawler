import urllib.request as req
import sys
from bs4 import BeautifulSoup

class ScrapCondition:
    def __init__(self,url):
        self.url = url
        res = req.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        #日付のスクレイピング
        days_list = soup.find_all("div", class_="ItemLink__info")
        #いいねのスクレイピング
        good_list = soup.find_all("ul" , class_="ItemLink__status")
        #リンクのスクレイピング
        link_list = soup.select(".media > div.media__body > div.ItemLink__title > a")
        #リストの初期化
        days = []
        year = []
        link = []
        good = []
        d_link = []
        g_link = []
        #リンクの取得
        for a in link_list:
            link.append(a.attrs['href'])
        for num in range(len(link_list)):
            #日付の精査
            days_list[num].a.decompose()
            days.append(days_list[num].text)
            word_d = str([days[num]])
            year.append(word_d[3:7])
            days_dict = {year[num]:link[num]}
            if year[num].isdigit():
                number_d = int(year[num])
                if number_d >= 2015:
                    d_link.append(days_dict[year[num]])
            #いいねの精査
            ward_g = str([good_list[num]])
            good_list[num].span.decompose()
            if "fa-comment-o" in ward_g:
                good_list[num].a.decompose()
                good.append(good_list[num].text)
            else:
                good.append(good_list[num].text)
            good_dict = {good[num]:link[num]}
            number_g = int(good[num])
            if number_g > 100:
                g_link.append(good_dict[good[num]])
        #リンクの結合
        days_set = set(d_link)
        good_set = set(g_link)
        self.select_link = list(days_set & good_set)
    def output(self):
        return(self.select_link)
