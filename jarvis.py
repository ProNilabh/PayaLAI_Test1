import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.runAndWait()
#print(voices)
engine.setProperty('Voice', voices[1
].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Payal Sir. How may I make your life better")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenting...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #logic for exectuting task
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wkikipedia")
            print(results)
            speak(results)

        elif "Open YouTube" in query:
            webbrowser.open("youtube.com")

        elif "Open Google" in query:
            webbrowser.open("google.com")

        elif "Open Github" in query:
            webbrowser.open("github.com")