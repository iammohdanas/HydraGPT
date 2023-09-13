
# from Brain.Qna import QuestionAnswer
import os
import random
import sys
import webbrowser
from requests import get
from Automations.translator import langtranslator
from Automations.whatsapp import sendWhatsappMsg
from Automations.youtube import openyoutube
from Arms.heart import predictHeartDisease
from Arms.bmrcalculator import bmrCalculate
from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting the Hydra : Wait for Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting the Hydra : Wait for few Seconds")
# from Main import MainTaskExecution




def MainExecution():
    Speak("Main Execution has been Started")
    Speak("Hello Sir, I am Hydra, I am ready to assist you sir")
    while True:
        # query = Listen().lower()
        # print(query)
        # if "hello" in query:
        #     Speak("Hi! I am Hydra")
        # else:
        #     Speak("Bye sir!")
        Data = MicExecution()
        Data = str(Data).lower()
        
        # ValueReturn = MainTaskExecution(Data)
        
        if len(Data)<3:
            pass
        # elif ValueReturn==True:
        #     pass
        elif "turn on the tv" in Data:
            Speak("Ok Turning on the TV")
        # elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
        #     Reply = QuestionAnswer(Data)
        elif 'play song' in Data:
                music_dir= "F:\\Songs\\New 2016"
                songs = os.listdir(music_dir)
                rd= random.choice(songs)
                os.startfile(os.path.join(music_dir,rd))
        elif "ip address" in Data:
                ip = get('https://api.ipify.org').text
                Speak("Here's your IP Address on the Screen : \n")
                print(ip)
        elif 'open facebook' in Data:
            webbrowser.open('wwww.facebook.com')
        elif "open youtube" in Data:
                openyoutube()
        elif "whatsapp" in Data:
            sendWhatsappMsg()
        elif "use translator" in Data:
             langtranslator()
             pass
        elif "sleep" in Data:
            Speak('thanks for using me sir, have a good day')
            sys.exit()
        elif "open heart disease prediction" in Data:
            Speak("Sure sir, Please wait for a while. it takes few seconds.")
            Speak("Enter the Required Data below")
            predictHeartDisease()
        elif "calculate body metabolism rate" in Data:
             Speak("Okay sir, Please provide me the details below")
             bmrCalculate()
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    # if "True-Mic" in query:
    #     print("")
    #     print(">> Clap Detected!!  >>")
    #     print("")
    #     MainExecution()

    # else:
    #     pass
    print("")
    print(">> Clap Detected!!  >>")
    print("")
    MainExecution()




ClapDetect()