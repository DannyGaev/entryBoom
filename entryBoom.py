import termcolor
import pyfiglet
import time
import threading
import requests
import argparse
from formScrape import *
from boomGens import *
from missile import *

#             _                ____   ___   ___  __  __
#            | |              |  _ \ / _ \ / _ \|  \/  |
#   ___ _ __ | |_ _ __ _   _  | |_) | | | | | | | \  / |
#  / _ \ '_ \| __| '__| | | | |  _ <| | | | | | | |\/| |
# |  __/ | | | |_| |  | |_| |_| |_) | |_| | |_| | |  | |
#  \___|_| |_|\__|_|   \__, (_)____/ \___/ \___/|_|  |_|
#                       __/ |
#                      |___/

if __name__ == '__main__':
    ascii_banner = pyfiglet.figlet_format("entry.B00M", font="big")
    colored_ascii_art = termcolor.colored(ascii_banner, color='blue')
    print(colored_ascii_art)
    parser = argparse.ArgumentParser(
        description="Send thousands of POST requests to scammers' Google Forms")
    parser.add_argument('-u', dest="url", type=str, help='URL of the form')
    parser.add_argument('-n', dest="num", type=int,
                        help='Number of requests')
    parser.add_argument('-v', dest="verbose", default=False,
                        action='store_true', help='Enable verbose mode')
    args = parser.parse_args()
    start = time.time()
    URL = str(args.url)
    URL = URL.replace("[.]", ".")
    payloads = args.num

    if "formResponse" not in URL:
        print("Reformatting the URL...")
        r = requests.get(URL)
        URL = r.url
        URL = URL[0:URL.find("viewform")]+"formResponse"

    entryIds, categories, answers = findFields(URL)
    createExample(entryIds, categories, answers)
    print(f"\nSending {
        payloads} payloads of randomly generated data to the form...")
    threads = []
    for _ in range(payloads):
        posting = threading.Thread(
            target=booming, args=(URL, entryIds, categories, answers, args, _))
        threads.append(posting)
        posting.start()
        time.sleep(0.1)
    for thread in threads:
        thread.join()
    end = time.time()
    getTable(start, end)
