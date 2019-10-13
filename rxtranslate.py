from scraper import *
from snapshot import *
from vision import *
from translate import *
from words import *
import json
import re

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

TakeSnapAndSave()
text = detect_text("/Users/tiff/GitHub/RxTranslate/resources/snapshot.jpg")
trans(text, "es")
for word in text.split(' '):
    if scrape(word.lower()) != False and not hasNumbers(word.lower()):
        synonyms = json.loads(getSynonyms(word.lower()))
        notDrug = False
        try:
            if len(synonyms["synonyms"]) < 5:
                for syn in synonyms["synonyms"]:
                    if scrape(syn) == False:
                        notDrug = True
                if notDrug == False:
                    print(scrape(word.lower()))
                    break
        except KeyError:
            pass

