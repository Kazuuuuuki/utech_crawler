mport urllib.request as req
import sys
from bs4 import BeautifulSoup

class ScrapDays:

    def __init__(self,url):
        self.url = url
        res = req.urlopen(url)
        soup = BeautifulSoup(res, "html.parser")
        days = []
        year =[]
        link = []
        self.select_link = []
        days_list = soup.find_all("div", class_="ItemLink__info")
        link_list = soup.select(".media > div.media__body > div.ItemLink__title > a")
        for a in links_list:
            link.append(a.attrs['href'])
        for num in range(len(link_list)):
            days_list[num].a.decompose()
            days.append(days_list[num].text)
            word = str([days[num]])
            year.append(word[3:7])
            dict_link = {year[num]:link[num]}
            number = int(year[num])
            if number >= 2014:
                self.select_link.append(dict_link[year[num]])
    def output(self):
        print(self.select_link)
