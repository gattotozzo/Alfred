import speech_recognition as sr

class CommandListener:
    def __init__(self, language):
        self.language = language
        self.recognizer = sr.Recognizer()

    def get_command(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio, language=self.language).lower()
        except sr.UnknownValueError as e:
            print("error while trying to recongize the command")
            return ""
        except sr.RequestError as e:
            print("Could not reach the google servers")
            return ""
        return text