from gtts import gTTS
import os

myText = "hello"

language = 'en'

output = gTTS(text=myText, lang=language)

output.save("output.mp3")

os.system("start output.mp3")

