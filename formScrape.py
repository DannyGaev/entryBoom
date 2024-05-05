from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re
import json
from boomGens import *
from missile import *


def findFields(URL):
    entryIds = []
    categories = []
    answers = []
    options = Options()
    tor_proxy = "127.0.0.1:9150"
    options.add_argument('--proxy-server=socks5://' + str(tor_proxy))
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    URL2 = "https://api.ipify.org/?format=json"
    driver.get(URL2)
    going = True
    while going:
        ip = driver.find_element("xpath", '//pre')
        if ip is not None:
            going = False
    print(f"Proxy IP: {json.loads(ip.text)["ip"]}")
    driver.get(URL)
    time.sleep(1)

    entries = driver.find_elements("xpath", '//div[@jsmodel="CP1oW"]')
    for entry in entries:
        newAnswer = [[], []]
        attrs = entry.get_attribute('data-params')
        attrs = attrs[attrs.index("[["):attrs.index("]]")].split(",")
        params = entry.get_attribute('data-params').split(",")
        # print(params)
        # print(int(params[3]))
        # print(' yahoo'.isdigit())
        searching = True
        c = 1
        while(searching):
            if params[c].isdigit():
                numAnswers = int(params[c])
                searching = False
            c+=1;

        entryIds.append(params[4][2:])
        categories.append(params[1])
        newAnswer[0] = numAnswers
        if numAnswers > 0:
            for attr in attrs:
                attribute = attr.replace("[", "")
                if "[" in attr and attr != "[" and attribute not in entryIds:
                    newAnswer[1].append(attribute)
        answers.append(newAnswer)

    return entryIds, categories, answers


def createExample(entryIds, categories, answers):
    key_replacements = {}
    examplePayload = genPayload(
        entryIds, categories, answers, get_tor_session(), get_user_agent())
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
