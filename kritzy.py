import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning!")

    elif(hour >= 12 and hour < 16):
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'm Kritzy. How can I help you?")

def introduceMe():
    speak("This is Gaayathri Suresh, a third year Bachelor of Technology student with Computer Science and Engineering as specialization. I've completed my eleventh and twelvth in KV and my scooling in NCS. I'm a passionate coder and a keen learner.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True: 
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif "open geeksforgeeks" in query:
            speak("Opening geeksforgeeks")
            webbrowser.open("geeksforgeeks.org")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")  

        elif "introduce me" in query:
            introduceMe()