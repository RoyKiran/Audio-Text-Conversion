# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:58:17 2017
@author: RK

Title: Google Speech Recognition: Text to Speech 
"""

import speech_recognition as sr

# Use audio Audio File as input to Google Speech Recognition 
from os import path
AUDIO_FILE =  path.join(r'<path to audio file>\xyz.wav')

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)        # Reads the entire source file

print("Audio Read completed.") 
 
#Speech recognition by google                    
try:
    print("Audio to text : \n",r.recognize_google(audio,language="hi-IN")) 
    
except sr.UnknownValueError:
    print("Google SR couldn't understand language")

except sr.RequestError as re:
    print("Couldn't request Google SR : {0}",format(re))
    
