from Body.ListenHindi import Listen
from Body.Speak import Speak
import googletrans
import gtts
# import pyttsx3()


def langtranslator():
    thisdict= googletrans.LANGUAGES
    Speak('In which language you want me to translate')
    lang = Listen().lower()
    translator = googletrans.Translator()
    if lang != None:
        Speak("Okay sir, what shall i translate for you")
        query = Listen().lower()
        if lang == "turkish":
            translation = translator.translate(query, dest='tr')
            print(translation)
            Speak(translation.text)
        elif lang == "french":
            translation = translator.translate(query, dest='fr')
            print(translation)
            Speak(translation.text)
        else:
            translation = translator.translate(query, dest="english")
            print(translation)
            Speak(translation.text)