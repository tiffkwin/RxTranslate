import requests
# import urllib.request
import time
from bs4 import BeautifulSoup

def scrape(drug):
    base_url = "https://webmd.com"
    url = "https://www.webmd.com/drugs/2/search?type=drugs&query="
    interactions_url = ""

    url = url + drug

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    atags = soup.findAll('a')
    for tag in atags:
        try:
            if tag["data-metrics-link"] == "result_1":
                interactions_url =  base_url + tag["href"] + "/list-interaction-medication"
                # print(base_url + interactions_url)
                break
        except KeyError:
            pass # or some other fallback action

    print(interactions_url)