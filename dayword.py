import json
from random_word import RandomWords
def get_day_word():
    r = RandomWords()
    day_data = r.word_of_the_day()
    json_converter = json.loads(day_data)#used to convert the string(day_data) to a json text
    word_of_the_day = json_converter.get('word')
    if type(day_data) is not None:
    
        print("Data Found")
    else:
        print("Try running again")
    return word_of_the_day

    
        
daily_word = get_day_word()
word_of_the_day = daily_word.upper()
print(f'Word Of the day : {word_of_the_day}')