import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty("rate", 178)

r = sr.Recognizer()
searchElement = ""
recognised_text = ""

while("alfred" not in recognised_text.lower()): 

    with sr.Microphone() as source:
        text = r.listen(source)

        try:
            recognised_text = r.recognize_google(text, language="it-IT")
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print("error")

    print(recognised_text)
    

with sr.Microphone() as source: 
    text = r.listen(source)
    try:
        recognised_text = r.recognize_google(text, language="it-IT")
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError as e:
        print("error")

try:
    recognised_text = r.recognize_google(text, language="it-IT")
except sr.UnknownValueError:
    print("error")
except sr.RequestError as e:
    print("error")

if ("Google" in recognised_text.lower()):
    if ("cerca" in recognised_text.lower()):
        i = recognised_text.find("cerca")+6
        
        for x in range (i, len(recognised_text)):
            searchElement += recognised_text[x]
        url = "https://www.google.com.tr/search?q=" + searchElement
        engine.say("subito, cerco " + searchElement + " su google!")
        engine.runAndWait()
    else:
        engine.say("no problem sir, you want something in particular?")
        engine.runAndWait()
        
        with sr.Microphone() as source: 
            text = r.listen(source)
            try:
                recognised_text = r.recognize_google(text, language="it-IT").lower()
            except sr.UnknownValueError:
                engine.say("i didn't understand sorry")
                engine.runAndWait()
            except sr.RequestError as e:
                engine.say("i didn't understand sorry")
                engine.runAndWait()
            if ("no" in recognised_text):
                url = "https://www.google.com"
                engine.say("ok, no problem. opening a new page")
                engine.runAndWait()
            else:
                url = "https://www.google.com.tr/search?q=" + recognised_text
                engine.say("perfect!")
                engine.runAndWait()
        
    webbrowser.open_new_tab(url)

elif ("spotify" in recognised_text):
    os.startfile("spotify:")