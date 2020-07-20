# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:04:11 2019

@author: shuvs
"""

import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver

num = 20
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("সহায়িকা : ", output) 
    
    
  
    toSpeak = gTTS(text = output, lang ='bn', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
    
def get_audio(): 
  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 2)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='bn-BD') 
        print("You : ", text) 
        return text 
  
    except: 
  
        assistant_speaks("আপনার কথা স্পষ্ট না, আবার চেষ্টা করুন!") 
        return 0

if __name__ == "__main__": 
    assistant_speaks("স্বাগতম") 
      
    while(1): 
  
        assistant_speaks("আমি আপনার জন্য কি করতে পারি") 
        text = get_audio() 
  
        if text == 0: 
            continue
        
        if "বিদায়" in str(text): 
            assistant_speaks("বিদায়") 
            break
        
        elif "কে তুমি" in str(text): 
            speak = "আমি আপনার  সহায়িকা"
            assistant_speaks(speak) 
  
        elif "তোমাকে কে বানিয়েছে "  in str(text): 
            speak = "আমাকে  বানিয়েছে শুভ সাহা"
            assistant_speaks(speak)
  

  
