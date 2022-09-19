import string
import random 
N = 5
cap = " ".join (random.choices(string.ascii_uppercase + string.digits, k = N))
print ("The generated random string : " + str(cap))


"""from gtts import gTTS
import os

language = "en"

myObj = gTTS(text = cap, lang = language, slow = True)
myObj.save ("Random.wav")
os.system ("Random.wav")
"""
captcha = input("Enter the captch you have listened: ")
#print (captcha)
if cap == captcha:
    print("True!")
else:
    print("try again!")

import speech_recognition as sr
#get audio from microphone
r = sr.Recoginzer()
with sr.Microphone() as source:
    print("Speak!")
    audio = r.listen(source)

try:
    print("You said " + r.recoginze_google(audio))
except sr.UnknownValueError:
    print("Couldn't Understand!")
except sr.RequestError as e:
    print("Couldn't request result; {0}".format (e))
