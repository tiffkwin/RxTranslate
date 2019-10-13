import requests

def getSynonyms(word):
    url = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/synonyms"

    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "fd3131b42bmshb666a819bee9b1fp1cdccbjsn31cd4460ae86"
        }

    response = requests.request("GET", url, headers=headers)

    return response.text