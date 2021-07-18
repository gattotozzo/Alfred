import webbrowser
import subprocess
import os
from AlfredTTS import AlfredVoice 
from SpeechRecognition import CommandListener

def main():

    searchElement = ""
    recognised_text = ""

    alfredVoice = AlfredVoice()
    commandListener = CommandListener("it-IT")

    while True:
        while True: 
            try:
                recognised_text = commandListener.get_command()
                print(recognised_text)
                if ("alfred" in recognised_text or "alfredo" in recognised_text):
                    break
            except Exception as e:
                print(e)
        print("WAKEWORD")

        if ("google" in recognised_text):
            if ("cerca" in recognised_text):
                i = recognised_text.find("cerca")+6
                for x in range (i, len(recognised_text)):
                    searchElement += recognised_text[x]
                url = "https://www.google.com.tr/search?q={}".format(searchElement)
                alfredVoice.speak("subito, cerco {} su google!".format(searchElement))
            else:
                alfredVoice.speak("nessun problema, vuoi cercare qualcosa in particolare?")
                try:
                    recognised_text = commandListener.get_command()
                except commandListener.UnknownValueError:
                    alfredVoice.speak("Scusa, non ho capito")
                except commandListener.RequestError as e:
                    alfredVoice.speak("Scusa, non ho capito")
                if ("no" in recognised_text):
                    url = "https://www.google.com"
                    alfredVoice.speak("ok, nessun problema")
                else:
                    url = "https://www.google.com.tr/search?q={}".format(recognised_text)
                    alfredVoice.speak("perfect!")
            webbrowser.open_new_tab(url)
        elif ("apri" in recognised_text):
            os.startfile("{}:".format(recognised_text.split("apri")[1].split()[0].replace(" ", "")))
        else:
            alfredVoice.speak("Scusa, non ho capito")
        recognised_text = ""

if __name__ == "__main__":
    main()