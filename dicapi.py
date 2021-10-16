import json,requests
url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"
def get_meaning(word):
    api_url = url + word
    word_data = requests.get(api_url).json()
    return word_data