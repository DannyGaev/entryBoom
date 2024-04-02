from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re
import json
from boomGens import *
from entryBoom import get_tor_session, get_user_agent


def getSoup(link):
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    time.sleep(12)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")
    return soup


def findFields(soup):
    pattern = r'<div[^>]*>(.*?)</div>'
    pattern2 = r'\[\[.*?]]'
    pattern3 = r'"(.*?)"'

    entryIds = []
    categories = []

    hidden_tags = soup.find_all("div", {"class": "Qr7Oae"})
    for tag in hidden_tags:
        tagBlock = str(tag)
        tagBlockContent = re.findall(pattern, tagBlock, re.DOTALL)

        entry = re.findall(pattern2, tagBlockContent[0], re.DOTALL)
        indexOfEntry = tagBlockContent[0].find(entry[0])
        splicedEntry = entry[0].split(",")[0].replace('[[', '')

        entryNum = splicedEntry
        categoryBlock = tagBlockContent[0][0:indexOfEntry]
        try:
            category = re.findall(pattern3, categoryBlock, re.DOTALL)[0]
        except:
            category = ""

        entryIds.append(entryNum)
        categories.append(category)

    return entryIds, categories

def scrapeForm(URL):
    print(f'\nWebscraping the Google Form at: "{URL}"')
    entryIds, categories = findFields(getSoup(URL))
    key_replacements = {}
    examplePayload = genPayload(
        entryIds, categories,  get_tor_session(), get_user_agent())
    values = []
    cnt = 0
    for key, value in examplePayload.items():
        values.append(value)

    print("\nCategories found: ")
    for category in categories:
        c = category.replace("\\n", '')
        key_replacements[c] = values[cnt]
        print("\t∙ {cat}".format(cat=c))
        cnt += 1

    print("\n\033[36mExample of a payload being sent to the form\033[39m: ")
    pretty_json = json.dumps(key_replacements, indent=4)
    print(f"\033[33m{pretty_json}\033[39m")
    return entryIds, categories
