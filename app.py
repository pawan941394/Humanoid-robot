import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from countryinfo import CountryInfo
listener =  sr.Recognizer()
engine =  pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.say('Hello my name is Robot what can i do for you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_commands():
    try: 
        with sr.Microphone(device_index = 2) as source:
            print("Listening --------------")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command =command.lower()
            if 'hi robo' in command:
                command = command.replace("robo", '')
            else:
                command  = "Please say my name first"
            return command
                
    except:
        command = "robo is not able to listen Please Try again after some time"
        return command
    
def run_robo():
    command =  take_commands()
    print(command)
    if 'robo' not in command:
        command =  command.replace('play','')
        talk('playing'+ command)
        pywhatkit.playonyt(command)
        talk(command)
    elif 'play' in command:
        command =  command.replace('play','')
        talk('playing'+ command)
        pywhatkit.playonyt(command)
   
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The current time is "+ time)
    elif 'who is' in command:
        person =  command.replace('robo who is', '')
        info =  wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'hello' in command:
        print(command)
        talk('hello sir')    
           
        talk('Have a good day !')

    elif 'bye' in command:
        quit
    elif "how are you" in command:
        print(command)
        talk("I am fine")
    elif "what is country of" in command:
        
        command =  command.replace('robo what is country of ','')
        country =  CountryInfo(command)
        country_is  =  country.capital()
        talk(f"The country of {command} is {country_is}")
    elif 'news headlines' in command:
        command =  command.replace('robo news headlines', '')
        talk("top headlines are ")
        news_headlines = []
        res = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey=d6feba03979147169d02e20f2c7779e2&category=general").json()
        articles = res["articles"]
        for article in articles:
            news_headlines.append(article["title"])
        for i in news_headlines[:5]:
            talk(i)
            
    
    elif 'weather' in command:
        talk('weather report of jaipur is ---- ')
        res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q=jaipur&appid=5adfabc98f7f2861feff07f5817dd237&units=metric").json()
 
        temperature = res["main"]["temp"]
    
        talk(  f" The weather temperature is  {temperature}℃")
        
    elif 'give me some advice' in command:
        res = requests.get("https://api.adviceslip.com/advice").json()
        talk('I think you should '+ res['slip']['advice'] )
    # elif 'how are you doing':
        # print(command)
        # talk('i am doing good thanks for asking')
    else:
        talk("please say the command again i am not able to understand")
while True:
    run_robo()