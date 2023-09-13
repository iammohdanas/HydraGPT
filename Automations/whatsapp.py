import datetime , timedelta
import pywhatkit as kit
from Body.Speak import Speak
from Body.Listen import MicExecution

def sendWhatsappMsg():
    Speak("Could you please provide me the phone number with country code :")
    phone_no = input("Enter Number :")
    Speak("okay sir, what message you want to send")
    message = MicExecution()
    print(message)
    hour = datetime.datetime.now().hour
    min1 = datetime.datetime.now().minute
    min2= min1 + 1
    kit.sendwhatmsg(phone_no,message,hour,min2)

