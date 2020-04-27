import speech_recognition as sr
from gtts import gTTS #google text to speech api
import pyaudio
import playsound
import datetime
import random
import time
import os

currentDir = os.getcwd()
print(currentDir)


def speek(textToRead):
    print(textToRead)
    talker = gTTS(text = textToRead, lang = "en")
    randomNum = random.randint(1,10000000000)
    fileName = str(randomNum) + ".mp3"
    talker.save(fileName) #save audio file to location
    playsound.playsound(fileName) #play the file
    os.remove(fileName) #remove the file

def recordSpeech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        text = "Please say something!"
        speek(text)
        audio = recognizer.record(source, duration=3)
    try:    
        audioData = recognizer.recognize_google(audio)
        print(audioData)
        return audioData
    except sr.UnknownValueError:
        text = "Oops, I didn't get that!"
        speek(text)

    except sr.WaitTimeoutError:
       text = "Oops, I didnt quite catch what you said!"
       speek(text)
    


def userNeedsWhat(audioData):
    if "weather" in audioData or "whether" in audioData:
        return "weather"
    if "date" in audioData:
        return "date"
    if "time" in audioData:
        return "time"
    if "exit" in audioData:
        return "exit"

def userNeedsWeather():
    text = "Weather today is really nice!"
    speek(text)

def userNeedsDate():
    today = datetime.date.today() #for use when user wants to know current date
    text = "Date today is " + today.strftime("%B %d, %Y")
    speek(text)

def userNeedsTime():
    now = datetime.datetime.now() #for use when user wants to know current time
    text = "The time is now " + str(now.strftime("%H:%M:%S"))
    speek(text)

def userNeedsExit():
    text = "Bye!"
    speek(text)
def startProgram():
    while True:
        try:
            audioData = recordSpeech()

        except UnboundLocalError():
            continue
        if audioData != None:
            #check if audioData contains valid data
            if "exit" in audioData:
                exit()
            userNeeds = userNeedsWhat(audioData)
            if userNeeds == "weather":
                userNeedsWeather()

            if userNeeds == "time":
                userNeedsTime()

            if userNeeds == "date":
                userNeedsDate()


startProgram()

