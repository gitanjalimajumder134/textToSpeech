from gtts.tts import gTTS
import os


mytext = 'My Name is Gitanjali Majumder'
language = 'en'

obj = gTTS(text= mytext, lang=language, slow = False)

obj.save("speech.mp3")

os.system("speech.mp3")