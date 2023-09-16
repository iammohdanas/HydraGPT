
# from Brain.Qna import QuestionAnswer
import os
import random
import sys
import webbrowser
from requests import get
from Automations.translator import langtranslator
# from Automations.whatsapp import sendWhatsappMsg
# from Automations.youtube import openyoutube
# from Arms.heart import predictHeartDisease
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
    # elif "open youtube" in Data:
    #         openyoutube()
    # elif "whatsapp" in Data:
    #     sendWhatsappMsg()
    elif "use translator" in Data:
            langtranslator()
            pass
    elif "sleep" in Data:
        Speak('thanks for using me sir, have a good day')
        sys.exit()
    elif "open heart disease prediction" in Data:
        Speak("Sure sir, Please wait for a while. it takes few seconds.")
        Speak("Enter the Required Data ")
        webbrowser.open("https://heart-disease-prediction-by-anas.streamlit.app/")
        # predictHeartDisease()
    elif "fit fuel" in Data:
            Speak("Okay sir, Please provide me the details ")
            webbrowser.open("https://metabomate.streamlit.app/")
    else:
        Reply = ReplyBrain(Data)
        Speak(Reply)

def tutorial():
     st.write("open heart disease prediction")
     


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

import streamlit as st
st.set_page_config(
    page_title="Voice Assistant",
    page_icon="🔊"
)
st.title("HydraGPT - Your Futuristic Voice Assistant ")
st.write("The only Voice Assistant which is compatible to work on machine learning models like heart disease prediction and Nutri-Tracker as well. The voice assistant demonstrates proficiency in speech recognition and executes various tasks upon user command, showcasing advanced programming and AI skills.")
custom_css = """
<style>
body {
    background-image: url('https://previews.123rf.com/images/peshkov/peshkov1802/peshkov180200477/96459742-abstract-ai-lamp-on-blue-background-artificial-intelligence-and-science-concept-3d-rendering.jpg');
    background-size: cover;
    color: #D3D3D3;
}
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Add a title and an image
st.image("mainimg.jpg", caption="Unlock the Power of AI. Soon, it will support the Stock Market Forecasting model. We are working on it", use_column_width=True)

# Add a button to trigger the assistant
if st.button("Run"):
    response = MainExecution()
    st.write(f"**Assistant:** {response}")




if st.button("Voice Commands :"):
    st.markdown("""
    <div id="bottom-sheet" style="
        position: relative;
        bottom: 0;
        left: 0;
        width: 100%;
        font-size: 12.5px;
        background-color: #f3f3f3;
        padding: 15px;
        border-top: 1px solid #ccc;
        ">
        <table style="border-collapse: collapse; width: 100%;"><tbody><tr><th style="border: 1px solid black; padding: 8px; text-align: left; background-color: rgb(242, 242, 242);">Function</th><th style="border: 1px solid black; padding: 8px; text-align: left; background-color: rgb(242, 242, 242);">Key</th></tr><tr><td style="border: 1px solid black; padding: 8px;"><b>Heart Disease Prediction Model</b></td><td style="border: 1px solid black; padding: 8px;">open heart disease prediction</td></tr><tr><td style="border: 1px solid black; padding: 8px;"><b>Calculates your Body Metabolism Rate</b></td><td style="border: 1px solid black; padding: 8px;">Open FitFuel</td></tr></tbody></table>        
    </div>
    <script>
        function closeBottomSheet() {
            location.reload();
        }
        
        setTimeout(function() {
            closeBottomSheet();
        }, 1000);
    </script>
    """, unsafe_allow_html=True)
# Add a footer
st.markdown("---")
st.write("Developed by - Mohd Anas Ansari")


# ClapDetect()