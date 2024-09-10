import termcolor
import pyfiglet
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time 
import threading
import requests
from requests.exceptions import ConnectionError
import json
import argparse
from tabulate import tabulate
from formScrape import *
from boomGens import *


#             _                ____   ___   ___  __  __
#            | |              |  _ \ / _ \ / _ \|  \/  |
#   ___ _ __ | |_ _ __ _   _  | |_) | | | | | | | \  / |
#  / _ \ '_ \| __| '__| | | | |  _ <| | | | | | | |\/| |
# |  __/ | | | |_| |  | |_| |_| |_) | |_| | |_| | |  | |
#  \___|_| |_|\__|_|   \__, (_)____/ \___/ \___/|_|  |_|
#                       __/ |
#                      |___/


successful = 0
denied = 0


def get_user_agent():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value,
                         OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agents = user_agent_rotator.get_user_agents()
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent


def get_tor_session():
    session = requests.session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session


def getTable(start, end):
    data = [
        ["Successful requests",
            f"\033[32m{successful}\033[39m"],
        ["Requests denied", f"\033[31m{denied}\033[39m"],
        ["Time elapsed (seconds)",
         f"\033[36m{end-start:.2f}\033[39m"]
    ]
    headers = ["Statistic", "Count"]
    table = tabulate(data, headers=headers, tablefmt="grid")
    print("\n"+table)


def booming(URL, entryIds, categories, answers, args, _):
    global successful, denied, verbose
    try:
        user_agent = get_user_agent()
        session = get_tor_session()
        r = session.get("http://httpbin.org/ip")
        while (not r):
            r = session.get("http://httpbin.org/ip")
        data = json.loads(r.text)
        payload = genPayload(entryIds, categories,
                             answers, session, user_agent)
        response = session.post(URL, data=payload, headers={
                                'User-Agent': user_agent})

        match response.status_code:
            case 200:
                status_code = "\033[32m200 (Successful)\033[39m"
                successful += 1
            case 400:
                status_code = "\033[31m400 (Bad Request)\033[39m"
                denied += 1
            case 401:
                status_code = "\033[31401 (Unauthorized)\033[39m"
                denied += 1
            case 403:
                status_code = "\033[31m403 (Forbidden)\033[39m"
                denied += 1
            case 404:
                status_code = "\033[31m404 (Not Found)\033[39m"
                denied += 1
            case 429:
                status_code = "\033[31m429 (Too Many Requests)\033[39m"
                denied += 1
            case 500:
                status_code = "\033[31m500 (Internal Server Error)\033[39m"
                denied += 1
            case 503:
                status_code = "\033[31m503 (Service Unavailable)\033[39m"
                denied += 1
            case 504:
                status_code = "\033[31m504 (Gateway Timeout)\033[39m"
                denied += 1

        if args.verbose:
            print("\033[1m✉️ Payload {number}\033[0m: \n\t\n\t\033[2m|User Agent: {userAgent}\n\t|IP Address of proxy: {ipAddr}\n\t|POST request response: {stat_code}\033[0m".format(
                number=_, userAgent=user_agent, ipAddr=data['origin'], stat_code=status_code), end="\n")

    except ConnectionError as e:
        if args.verbose:
            status_code = "\033[31mRemote End Closed Connection Without Response\033[39m"
            print("\033[1m✉️ Payload {number}\033[0m: \n\t\n\t\033[2m|User Agent: {userAgent}\n\t|IP Address of proxy: {ipAddr}\n\t|POST request response: {stat_code}\033[0m".format(
                number=_, userAgent=user_agent, ipAddr=data['origin'], stat_code=status_code), end="\n")
        denied += 1
