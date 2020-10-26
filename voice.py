from gtts import gTTS
from time import sleep
import os
import pyglet
import playsound
def voice(text,num):
    tts = gTTS(text=text, lang='en')
    filename = str(num)+'.mp3'
    tts.save(filename)
    playsound.playsound(filename)   

