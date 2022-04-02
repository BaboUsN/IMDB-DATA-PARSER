import time
from bs4 import BeautifulSoup
import requests
import json


def getDataWithCurrentUrl(num):

    def getSiteData(num):
        data = requests.get(
            f"https://www.imdb.com/search/title/?groups=top_1000&start={num}&ref_=adv_nxt")
        return (str(data.content))
    text = getSiteData(num)
    with open("sitedata.txt", "w+", encoding="utf-8") as file:
        file.write(text)
    lenOfData = len(str(text))
    input("There are {lenOfData} char data")


def getDataWithNewUrl(url):

    def getSiteData(url):
        data = requests.get(url)
        return (str(data.content))
    text = getSiteData(url)
    with open("sitedata.txt", "w+", encoding="utf-8") as file:
        file.write(text)
    lenOfData = len(str(text))
    input("There are {lenOfData} char data")
