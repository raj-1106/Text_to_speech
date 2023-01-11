import string
import random 
N = 5 
# N is used for size of string 
cap = " ".join (random.choices(string.ascii_uppercase + string.digits, k = N)) # the random function will generate random string everytime when we refresh the screen or run the program
print ("The generated random string : " + str(cap))
# This function will generate a random string which we can use for captcha  

import pyttsx3
# pyttsx3 is an api which will convert our following string into sound format
engine = pyttsx3.init()

engine.say(cap)
# this command will speak our string
newVoiceRate = 200
engine.setProperty('rate',newVoiceRate)
# engine.say("What can i do for you!")
engine.runAndWait()
engine.stop()

 #Now we will take input in form of text frpm user 
captcha=input("Enter the captch you have listened: ")
if captcha == cap :
    print("True!")
else:
    print("try again!")  

# This API will be used for taking user's speech input and check it with the captcha
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while (1):
    try: 
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration = 0.2)

            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say  "+MyText)
            SpeakText(MyText)
    except sr.RequestError as e:
        print("Couldn't request result: {0}".format(e))
    
    except sr.UnknownValueError:
        print("Couldn't hear you please speak again")
        SpeakText("Couldn't hear you please speak again")
#Now this condition will check the user's speech input with our predefine captcha
if MyText == cap:
    print("You may continue")
else :
    print("Please Try Again")