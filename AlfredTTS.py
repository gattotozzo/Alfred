import pyttsx3

class AlfredVoice:

    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty("rate", 170)
    
    def speak(self, phrase):
        print(f"[TTS]: {phrase}")
        self.engine.say(phrase)
        self.engine.runAndWait()