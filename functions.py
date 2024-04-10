import speech_recognition as sr
import pyttsx3
from datetime import datetime

voice_engine = pyttsx3.init()
HOUR = datetime.now().hour
MIN = datetime.now().min

# to make it speak 

voices = voice_engine.getProperty('voices')
voice_engine.setProperty('voice', voices[2].id) 






def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 4
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        query = "pepperstone didnt hear what the user said say that to the user"
    return query

def speak(text):
    print(f"PepperStone:{text}")
    voice_engine.say(text)
    voice_engine.runAndWait()

def wishMe():
    if HOUR >=0 and HOUR <12:
        speak("Good morning Sanketh sir")

    elif HOUR >=12 and HOUR <18:
        speak("Good afternoon Sanketh sir")
    
    else:
        speak("Good evening Sanketh sir")
    speak("feel free to ask me anything...")
    


