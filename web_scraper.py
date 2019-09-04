import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["StarTrekScripts"]
the_original_series_col = db["TheOriginalSeries"]
the_next_generation_col = db["TheNextGeneration"]
deep_space_nine_col = db["DeepSpaceNine"]
voyager_col = db["Voyager"]

URL = "http://www.chakoteya.net/StarTrek/episodes.htm"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
episodes = {}
for table in soup.find("table").find_all("table")[:3]:
    for row in table.find_all("tr"):
        if (row.find_all("td")[0].find("a") != None):
            episode = row.find_all("td")[0].find("a")
            episodes[episode.text] = episode.get("href")
for episode, link in episodes.items():
    URL = "http://www.chakoteya.net/StarTrek/" + link
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    the_original_series_col.insert_one({"episode": episode.strip(), "script": soup.find("table").get_text()})

URL = "http://www.chakoteya.net/NextGen/episodes.htm"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
episodes = {}
for table in soup.find("table").find_all("table"):
    for row in table.find_all("tr"):
        if (row.find_all("td")[0].find("a") != None):
            episode = row.find_all("td")[0].find("a")
            episodes[episode.text] = episode.get("href")
for episode, link in episodes.items():
    URL = "http://www.chakoteya.net/NextGen/" + link
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    the_next_generation_col.insert_one({"episode": episode.strip(), "script": soup.find("table").get_text()})

URL = "http://www.chakoteya.net/DS9/episodes.htm"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
episodes = {}
for table in soup.find("table").find_all("table"):
    for row in table.find_all("tr"):
        if (row.find_all("td")[0].find("a") != None):
            episode = row.find_all("td")[0].find("a")
            episodes[episode.text] = episode.get("href")
for episode, link in episodes.items():
    URL = "http://www.chakoteya.net/DS9/" + link
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    deep_space_nine_col.insert_one({"episode": episode.strip(), "script": soup.find("table").get_text()})

URL = "http://www.chakoteya.net/Voyager/episode_listing.htm"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
episodes = {}
for table in soup.find("table").find_all("table"):
    for row in table.find_all("tr"):
        if (row.find_all("td")[0].find("a") != None):
            episode = row.find_all("td")[0].find("a")
            episodes[episode.text] = episode.get("href")
for episode, link in episodes.items():
    URL = "http://www.chakoteya.net/Voyager/" + link
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    voyager_col.insert_one({"episode": episode.strip(), "script": soup.find("table").get_text()})
