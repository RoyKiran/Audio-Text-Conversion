
# -*- coding: utf-8 -*-
"""
@author: RK
--- Title: Google Speech Recognition : Speech To Text -----
"""

import speech_recognition as sr

r = sr.Recognizer()                 # Get an instance of Speech Recognizer
#print(sr.Microphone()!= None)      # Check if microphone is present


with sr.Microphone() as source:     # Get access to Microphone
    print("Begin recording")
    audio = r.listen(source)        # Start listening through Microphone


try:
    print(r.recognize_google(audio)) # Google API starts recognizing the audio

except sr.UnknownValueError:    
    print("Google SR couldn't understand language")

except sr.RequestError as re:  # Throw error for No Connection to Google API
    print("Couldn't request Google SR : {0}",format(re))


