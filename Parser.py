import time
from bs4 import BeautifulSoup
import requests
import json

doc = ""

with open("sitedata.txt", "r+", encoding="utf-8")as file:
    doc = file.read()


def parser(bs, div, classTitle):
    bsr = bs.find_all(f"{div}", {"class": f"{classTitle}"})
    return bsr


def InfoParser(bs):
    myDict = {}
    filmTitleAndYear = parser(
        bs, "h3", "lister-item-header")[0].text.replace("\\n", "").replace("\\n", "").replace("\\n", "").strip()
    # print(filmTitleAndYear)
    myDict["Title"] = filmTitle = filmTitleAndYear.split(
        ".")[1].split("(")[0].replace("\\n", "").replace("\\n", "").strip()
    myDict["Year"] = filmYear = filmTitleAndYear.split("(")[1].split(")")[
        0].replace("\\n", "").replace("\\n", "").strip()
    myDict["Runtime"] = filmRuntime = parser(
        bs, "span", "runtime")[0].text.replace("\\n", "").replace("\\n", "").strip()
    myDict["Genre"] = filmGenre = parser(bs, "span", "genre")[
        0].text.replace("\\n", "").replace("\\n", "").strip()
    try:
        myDict["Certificate"] = filmCertificate = parser(
            bs, "span", "certificate")[0].text.replace("\\n", "").replace("\\n", "").strip()
    except:
        myDict["Certificate"] = None
    myDict["ImbdRate"] = filmImbdRate = parser(
        bs, "div", "inline-block ratings-imdb-rating")[0].text.replace("\\n", "").replace("\\n", "").strip()
    try:
        myDict["Metascore"] = filmMetascore = parser(
            bs, "span", "metascore favorable")[0].text.replace("\\n", "").replace("\\n", "").strip()
    except:
        myDict["Metascore"] = None
    myDict["About"] = filmAbout = parser(
        bs, "p", "text-muted")[-1].text.replace("\\n", "").replace("\\n", "").strip()
    try:
        myDict["Director"] = filmDirector = parser(bs, "p", "")[0].text.replace(
            "\\n", "").split("Director:")[1].split("|")[0].replace("\\n", "").replace("\\n", "").strip()
    except:
        myDict["Director"] = None
    myDict["Stars"] = filmStars = parser(bs, "p", "")[0].text.replace(
        "\\n", "").split("Stars:")[1].replace("\\n", "").replace("\\n", "").strip()
    filmSubInfo = parser(
        bs, "p", "sort-num_votes-visible")[0].text.replace("\\n", "")
    if "Votes:" in filmSubInfo:
        myDict["Votes"] = filmVotes = filmSubInfo.split(
            "Votes:")[1].strip().split(" ")[0].replace("|", "").replace("\\n", "").replace("\\n", "").strip()
        # to indicate that it is working cause sometimes that's can be problem
        print(filmVotes)

    else:
        myDict["Votes"] = None

    if "Gross:" in filmSubInfo:
        myDict["Gross"] = filmGross = filmSubInfo.split(
            "Gross:")[1].strip().split(" ")[0].replace("|", "").replace("\\n", "").replace("\\n", "").strip()
    else:
        myDict["Gross"] = None

    if "Top 250:" in filmSubInfo:
        myDict["Top250"] = filmTop250 = filmSubInfo.split("Top 250:")[1].strip().split(" ")[
            0].replace("|", "").replace("\\n", "").replace("\\n", "").strip()
    else:
        myDict["Top250"] = None
    return myDict


def start():
    bs = BeautifulSoup(doc, 'html.parser')
    films = parser(bs, "div", "lister-item mode-advanced")
    arr = []
    for i in films:
        # convert to bs4 object
        arr.append(InfoParser(BeautifulSoup(str(i), 'html.parser')))
    jsonData = json.dumps(arr)

    with open("MovieData.json", "w+", encoding="utf-8") as file:
        file.write(jsonData)
