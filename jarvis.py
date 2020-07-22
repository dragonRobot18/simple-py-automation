import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
from win10toast import ToastNotifier
import time

# workon jarvis
# python jarvis.py

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hours = int(datetime.datetime.now().hour)
    if hours >= 0 and hours < 12:
        greeting_text = 'Good Morning, Have a Wonderful Day !'
    elif  hours >= 12 and hours < 18:
        greeting_text = 'Good Afternoon, Hope you are doing good !' 
    else:
        greeting_text = 'Good Evening, I hope you had a Good day !'
    toaster = ToastNotifier()
    toaster.show_toast("Jarvis",greeting_text)
    speak(greeting_text)


def voiceInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print('Listening ... ')
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        # print('Recognizing ... ')
        query = r.recognize_google(audio)
        # print(f'User said : {query}\n')
    except Exception as e:
        # print(e)
        # print('Please say that again !')
        return "None"

    return query

# def open_youtube():


if __name__ == "__main__":
    greetings()
    
    print('Hello say "jarvis"')
    while True:
        query = voiceInput().lower()
        if 'jarvis' in query:
            speak('How may I help you ?')
            query = voiceInput().lower()

            # tasks based on query
            if 'open youtube' in query:
                print('Opening YouTube ... \n')
                speak('Opening YouTube')
                webbrowser.open('https://www.youtube.com/')
                # https://www.youtube.com/results?search_query=python
            elif 'search on youtube' in query:
                print('What to search on youtube ?')
                speak('What to search on youtube ?')
                youtube_query = voiceInput().lower()
                print('Opening YouTube ...\n')
                speak('Opening YouTube')
                webbrowser.open('https://www.youtube.com/results?search_query={}'.format(youtube_query))
            elif 'open whatsapp' in query:
                wa_path = 'C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
                os.startfile(wa_path)
                print('Opening Whatsapp ... \n')
                speak('Opening Whatsapp')
                time.sleep(3)
            elif 'open cmd' in query:
                cmd_path = 'C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt'
                os.startfile(cmd_path)
            elif 'open coursera' in query:
                webbrowser.open('https://www.coursera.org/programs/kk-wagh-institute-of-engineering-on-coursera-ilu6j')
            elif 'search on google' in query:
                print('What to search on google ?')
                speak('What to search on google ?')
                google_query = voiceInput().lower()
                print('Opening Google ...\n')
                speak('Searching on Google !')
                webbrowser.open('https://www.google.com/search?client=firefox-b-d&q={}'.format(google_query))
                
            elif 'to do list' in query:
                with open ('todo.txt', 'r') as myfile:  # Open lorem.txt for reading text
                    contents = myfile.read()              # Read the entire file to a string
                    speak(contents)
                myfile.close()
                # speak('Do you to add some things ?') 
                # temp = voiceInput().lower()
                # if 'yes' in temp:
            # else:
            #     speak('Sorry , I did not understood what you want to say or may be requested function does not exist , Can you please repeat')
                # continue
            else:
                pass
        elif 'exit' in query:
            speak('See you soon')
            break