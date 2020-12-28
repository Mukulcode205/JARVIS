import pyautogui
import wikipedia
import random
import webbrowser
import pyttsx3
import speech_recognition as sr
def speak(a):
    # It gives output from mic interpretting user input
    return pyttsx3.speak(a)
def wishme():
    # wishes the user according to the time
    import datetime
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Goodmorning sir")
    elif hour >= 12 and hour <= 17:
        speak("good after noon sir")
    else:
        speak("Good evening sir")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:   
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query



def takeCommand2():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    return query
if __name__ == "__main__":
    wishme()
mean = takeCommand2().lower()
if 'jarvis' in mean:
    query = takeCommand().lower()
    if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
    if 'your name' in query:
        speak("My name is JARVIS a singlarity program")
    if 'nice' in query:
        speak('thank you for appericiation')
    if 'open youtube' in query:
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    if 'open gmail' in query:
        speak("opening Gmail")
        webbrowser.open("https://gmail.com")
    if 'open google' in query:
        speak("opening google")
        webbrowser.open("https://google.com")
    if 'open github' in query:
        speak("opening github.")
        webbrowser.open("https://github.com")
    if 'type' and 'write' and 'something' in query:
        speak("ok sir!")
        speak("you can start speaking the text")
        new1 = takeCommand().lower()
        print("User said: ", new1)
        pyautogui.typewrite(new1)
