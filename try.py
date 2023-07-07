import string
import random
import pyttsx3
import speech_recognition as sr

N = 5
cap = " ".join(random.choices(string.ascii_uppercase + string.digits, k=N))
print("The generated random string: " + cap)

engine = pyttsx3.init()
engine.say(cap)
newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)
engine.runAndWait()
engine.stop()

captcha = input("Enter the captcha you have listened: ")
if captcha == cap:
    print("True!")
else:
    print("Try again!")

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

num_iterations = 2  # Specify the desired number of iterations
iteration = 0  # Counter variable for iterations
response_timeout = 5  # Specify the response timeout in seconds

while iteration < num_iterations:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2, timeout=response_timeout)  # Set the timeout value
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say: " + MyText)
            SpeakText(MyText)
    except sr.RequestError as e:
        print("Couldn't request result: {0}".format(e))
    except sr.UnknownValueError:
        print("Couldn't hear you, please speak again")
        SpeakText("Couldn't hear you, please speak again")
    except sr.WaitTimeoutError:
        print("Time limit exceeded. Please speak within {} seconds.".format(response_timeout))
        SpeakText("Time limit exceeded. Please speak within {} seconds.".format(response_timeout))

    if MyText == cap:
        print("You may continue")
        break
    else:
        print("Please try again")

    iteration += 1  # Increment the iteration counter

print("Finished running the code two times")
