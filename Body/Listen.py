import speech_recognition as sr
from googletrans import Translator


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,10,3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")
        # print(f"User said: {query}\n")
    except Exception as e:
        print('Say that again please...')
        return ""
    
    query = str(query).lower()
    return query

    
def TranslationHintoEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    data = data.lower()
    print(f"You : {data}.")
    return data

def MicExecution():

    query = Listen()
    data = TranslationHintoEng(query)
    return data


# print(MicExecution())