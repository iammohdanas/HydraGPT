from Body.Listen import Listen
from Body.Speak import Speak
from Features.Clap import Tester
import speech_recognition as sr
import os

# def Main():
#     Tester()
#     Speak("Hello Sir!?")


data = Tester()
if "True-Mic" == data:
    from Hydra import MainExecution
    MainExecution()


























# if __name__ == "__main__":
#     Main()




# Wakeup Detector


# import speech_recognition as sr
# import os
# from Hydra import MainExe


# def Listen():
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source,0,3)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio,language="en")
#         # print(f"User said: {query}\n")
#     except Exception as e:
#         print('Say that again please...')
#         return ""
    
#     query = str(query).lower()
#     print(query)
#     return query

# def WakeupDetected():
#     queery = Listen().lower()

#     if "wake up" in queery:
#         MainExe()
#     else:
#         pass


# while True:
#     WakeupDetected()