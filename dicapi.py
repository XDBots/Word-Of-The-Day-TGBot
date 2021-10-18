import json,requests
url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"
def get_meaning(word):
    api_url = url + word
    #This statement will give us the json data of the request we made using the api_url.
    word_data = requests.get(api_url).json()
    return word_data
