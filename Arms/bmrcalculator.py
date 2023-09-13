import pyttsx3

def Speak(Text):
    engine = pyttsx3.init('sapi5')   #sapi5 helps google ko bulwane me
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty("rate", 170)
    print("")
    print(f"You : {Text}.")
    engine.say(Text)
    engine.runAndWait()

def bmrCalculate():
    weight = int(input("Enter your weight in KG: \n"))
    height = int(input("Enter your height in cm: \n"))
    age = int(input("Enter your age in years: \n"))
    isMale = str(input("Are you male? (y/n)"))

    if isMale == "y":
        isMale = True
    elif isMale == "n":
        isMale = False
    else:
        print("Error")
        quit()
        
        

    # Mifflin St. Jeor Equation for males
    if isMale:
        bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    else:
        bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    bmr = round(bmr)
    # print(bmr)
    Speak("Your bmr is :")
    Speak(bmr)
    Speak("Now answer some of the questions so that i can tell you the amount of macro nutrients ")
    weightmanage= str(input("Do you want to gain weight or lose weight?  Enter in (gain/loss) : "))
    calmanage = 200
    print("\nokay sir, i have provided you the maintenance calories below :\n")
    if weightmanage == "gain":
        print("You need to add ",calmanage,"daily to your diet plan and consume ",bmr+calmanage," calories\n")
    elif weightmanage == "loss":
        print("You need to add ",calmanage,"daily to your diet plan and consume ",bmr+calmanage," calories\n")
    else:
        print("Error")
        quit()

    calforweightloss = bmr - calmanage
    protein_for_loss = (calforweightloss/100)*35
    protein_for_loss_gm = ((calforweightloss/100)*35)/4
    carbs_for_loss = (calforweightloss/100)*50
    carbs_for_loss_gm = ((calforweightloss/100)*50)/4
    fat_need_for_loss = (calforweightloss/100)*15
    fat_need_for_loss_gm = ((calforweightloss/100)*15)/9

    calforweightgain = bmr + calmanage
    protein_for_gain = (calforweightgain/100)*35
    protein_for_gain_gm = ((calforweightgain/100)*35)/4
    carbs_for_gain = (calforweightgain/100)*50
    carbs_for_gain_gm = ((calforweightgain/100)*50)/4
    fatneed_for_gain = (calforweightgain/100)*15
    fatneed_for_gain_gm = ((calforweightgain/100)*15)/9


    if weightmanage == "gain":
        print("Calories from protein : ",protein_for_gain, " / ",protein_for_gain_gm,"gm")
        print("Calories from carbohyderates : ",carbs_for_gain, " / ",carbs_for_gain_gm,"gm")
        print("Calories from Fat : ",fatneed_for_gain, " / ",fatneed_for_gain_gm,"gm")

    elif weightmanage == "loss":
        print("Calories from protein : ",protein_for_loss, " / ",protein_for_loss_gm,"gm")
        print("Calories from carbohyderates : ",carbs_for_loss, " / ",carbs_for_loss_gm,"gm")
        print("Calories from Fat : ",fat_need_for_loss, " / ",fat_need_for_loss_gm,"gm")
    else:
        print("Error")
        quit()


# bmrCalculate()