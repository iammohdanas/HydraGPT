import datetime , timedelta
import pywhatkit as kit
from Body.Speak import Speak
from Body.ListenHindi import Listen
def openyoutube():
    Speak('okay sir, what you want to play?')
    song_name= Listen()
    Speak("okay sir, just a second")
    kit.playonyt(song_name)

