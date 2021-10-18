import json
from random_word import RandomWords
def get_day_word():
    #Calling the RandomWords function from random_word library.
    r = RandomWords()
    #To get the word of the day statement we use r.word_of_the_day()
    day_data = r.word_of_the_day()
    #Thia will be used to convert the string(day_data) to a json text
    json_converter = json.loads(day_data)
    word_of_the_day = json_converter.get('word')
    #Check if the day_data is None Type or not. Though Idk how I got error even after putting condition.
    if type(day_data) is not None:
        print("Data is Found")
    else:
        print("Try running again")
    #This Function will return us the word_of_the_day that we need, we can also take it's meaning, defination here but I'm trying get the meaning from the api I liked.
    return word_of_the_day
    

word = get_day_word()
#to make the word uppercase
word_of_the_day = word.upper()
print(f'Word Of the day : {word_of_the_day}')
