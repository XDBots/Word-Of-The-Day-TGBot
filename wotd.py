import telebot,requests,json
import schedule,dicapi
from dayword import word_of_the_day
bot = telebot.TeleBot("BOT_TOKEN")
api_url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,"Yo Dude Whats up!, Thanks for starting me, If you need any help contact my master @DebNationXD")


ids = ["-378428636","759684783","-1001343080295","-378428636"]
total_ids = len(ids)
@bot.message_handler(commands=['start'])

def send_text():
    for i in range(total_ids):
        bot.send_message(ids[i],f" Hello Sir🙏, Good Morning, Today's Word Of The Day is <b><i>{word_of_the_day}</i></b>, Have a Great Day👍 ",parse_mode = "HTML")
        if not word_of_the_day:
            bot.send_message(ids[i],"NO WORD OF THE DAY FOUND")
        else:
            wotd_data = dicapi.get_meaning(word_of_the_day)
            if isinstance(wotd_data,dict) and wotd_data['title']:
                bot.send_message(ids[i],"API Error, WOTD meaning not found!")
            else:
                means = wotd_data[0]['meanings']
                if len(means) == 0:
                    bot.send_message(ids[i],f' Word Of The Day(WOTD) Definition Not Found in API Database Regarding `{word_of_the_day}` .',parse_mode = "MARKDOWN")
                else:
                    meaning = means[0]['definitions'][0]['definition']
                    audio_data = wotd_data[0]['phonetics']
                    audio = audio_data[0].get('audio')
                    audio_format = "https:" + audio
                    
                    ex = wotd_data[0]['meanings'][0]['definitions'][0]
                    example = ex.get('example')
                    word = word_of_the_day.upper()
                    bot.send_message(ids[i],f'<b><i>{word_of_the_day}</i></b> -->>> <i><u>{meaning}</u></i>',disable_web_page_preview = True,parse_mode = "HTML")
                    
                    if example is not None and len(audio_data) != 0:
                        print(audio)
                        bot.send_message(ids[i],f'<b>Example</b> --> <i>{example}.</i>\n<a href="{audio_format}"> Pronounciation</a>',disable_web_page_preview = True,parse_mode="HTML")
                      
                    elif example is None and len(audio_data) != 0:
                        bot.send_message(ids[i],f'Sorry,Example Not Found.\n<a href="{audio_format}">Pronounciation</a>',disable_web_page_preview = True,parse_mode = "HTML")
                        
                    elif example is not None and len(audio_data) == 0:
                        bot.send_message(ids[i],f'<b>Example</b> --> <i>{example}.</i>\n Sorry No Pronunciation is Available.',parse_mode = "HTML")
                        
                    else:
                        bot.send_message(ids[i],'Sorry,Example and Pronounciation Not Available.')
schedule.every().day.at("00:09").do(send_text)

while True:
    schedule.run_pending()
                   
           
bot.polling()
