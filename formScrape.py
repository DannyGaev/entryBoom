from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re


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
        category = re.findall(pattern3, categoryBlock, re.DOTALL)[0]

        entryIds.append(entryNum)
        categories.append(category)

    return entryIds, categories
