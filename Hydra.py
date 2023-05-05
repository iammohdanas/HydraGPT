from Features.Clap import Tester


from Body.Speak import Speak


from Body.Listen import MicExecution
print(">> Starting the Hydra : Wait for Some Seconds.")
from Brain.AIBrain import ReplyBrain
from Features.Clap import Tester
print(">> Starting the Hydra : Wait for few Seconds")

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
        Reply = ReplyBrain(Data)
        Speak(Reply)


def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!!  >>")
        print("")
        MainExecution()

    else:
        pass

ClapDetect()