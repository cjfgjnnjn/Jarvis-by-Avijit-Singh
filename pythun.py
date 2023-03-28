# Jarvis by Avijit Singh
# This project's idea has been taken from a youtube cahnnel named "CODE WITH HARRY"
# NOTE - The function of this program have been written by me(Avijit Singh) only

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import random
import keyboard
import requests
import time
import pywikihow
from pywikihow import search_wikihow, HowTo
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
jarvis = "I am jarvis an virtual Ai,               "
'You know me as AI of Tony,               '
'But in past few moths i am getting operated by my new inventor, Mr.Avijit Singh,             '
'Now tell me how can i help you.'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
a = int(input("Which voice do you want?(male[0]/female(1)):"))

engine.setProperty('voice', voices[a].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def playmusic():
    import speech_recognition as sr
    import pyttsx3
    import pywhatkit

    def talk(command):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say('Playing ')
        engine.runAndWait()

    def takeCommand():
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                speak('Which music sir?')
                print("music name...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                song = command.replace('play', '')
                talk(song)
                pywhatkit.playonyt(song)

        except:
            pass

    takeCommand()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis an virtual Ai,               "
          "You know me as AI of Tony,               "
          "But in past few moths i am getting operated by my new inventor, Mr.Avijit Singh,             "
          "Now tell me how can i help you.")
def ytvideo():
    import speech_recognition as sr
    import pyttsx3
    import pywhatkit

    def talk(command):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say('Playing ' + command)
        engine.runAndWait()

    def takeCommand():
        listener = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                speak('Which content sir?')
                print("content name...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                song = command.replace('play', '')
                talk(song)
                pywhatkit.playonyt(song)

        except:
            pass

    takeCommand()
def wishyou():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def youtubesearch():
    pass

def googlesearch():
    speak('What should I search?')
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        search_query = r.recognize_google(audio)
        print(f"You said: {search_query}")
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open_new_tab(url)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError:
        print("Sorry, my speech service is down right now.")

def takeCommand():
    # It takes microphone input from the user and returns string output

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
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('avijitsingh2473@gmail.com', 'your_password')
    server.sendmail('avijitsingh2473@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak(f'Searching {speak(query)} in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'hello' in query:
            speak('hello sir')
        elif 'hi jarvis' in query:
            speak('hello sir')
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")
        elif 'quick search' in query:
            googlesearch()
        elif 'who are you' in query:
            speak(jarvis)

        elif 'feeling boring' in query:
            speak('ok sir I think you want me to play something on youtube?')
            speak('then tell me sir')
            ytvideo()
        elif 'about you' in query:
            speak(jarvis)
        elif ' about your developer' in query:
            speak("My developer is mr.Avijit Singh ")
            speak("Avijit Singh is a Python programmer, developer, and web3 enthusiast. He is a Solidity developer and has experience with Python and Flutter. He is currently working on Mongo-DB. In addition to his technical skills, Avijit is also an athlete and a musician. He has run 100m in 11.45 seconds and plays the guitar, focusing on fingerstyle, tabs, and chords. Avijit is from Indira Memorial English Medium High School"
                  "Avijit is actively involved in open-source projects on GitHub and regularly shares knowledge and insights with the community on social media platforms like GitHub and Twitter.")
        elif 'close this' in query:
            speak('ok sir')
            keyboard.press_and_release('ctrl+w')
        elif 'open setting' in query:
            speak('ok sir')
            keyboard.press_and_release('windows+i')
            # keyboard.press_and_release('c+a+m+e+r+a')
            # keyboard.press_and_release('enter')
        elif 'open stackoverflow' in query:
            speak('opening stckoverflow')
            webbrowser.open("stackoverflow.com")
        elif ' my mail' in query:
            speak("ok sir, Why not you check? here it's go")
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            speak('sir you are watching your mails of 2nd alpha administrator account of your system.'
                  'as iam not getting your 1st one. ')
        elif 'how to' in query:
            speak("Getting the dta from internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func: list[HowTo] = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        elif 'very good' in query:
            speak('thanks sir! Have any thing to ask for?')
        elif 'well done' in query:
            speak('thanks sir! Have any thing to ask for?')
        elif 'jarvis' in query:
            speak("yes sir how can i help you?")
        elif 'music' in query:
            playmusic()
            # speak('playing music')
        elif 'good morning' in query:
            wishyou()
        elif 'good evening' in query:
            wishyou()
        elif 'good afternoon' in query:
            wishyou()
        elif 'who is your developer' in query:
            speak('Mr.Avijit Singh')
            speak('if you want I can open his port folio websitr where you get all about him.')
            speak('Should I open it? yes or no')
        elif 'yes open it' in query:
            speak("Avijit's portfolio")
            webbrowser.open('https://pofoavijit.super.site/')
            speak(
                "Avijit Singh is a Python programmer, developer, and web3 enthusiast. He is a Solidity developer and has experience with Python and Flutter. He is currently working on Mongo-DB. In addition to his technical skills, Avijit is also an athlete and a musician. He has run 100m in 11.45 seconds and plays the guitar, focusing on fingerstyle, tabs, and chords. Avijit is from Indira Memorial English Medium High School"
                "Avijit is actively involved in open-source projects on GitHub and regularly shares knowledge and insights with the community on social media platforms like GitHub and Twitter.")

        elif ' my code space' in query:
            speak("Opening Avijit Singh's Github page")
            webbrowser.open('https://github.com/cjfgjnnjn')
            speak("Have a look on Mr.Avijit's repositories")
            speak(" have a view on the fantastic free python codes code by Avijit Singh")
            speak("Not surely but you will get 2 to 3 projects available on this github page in upcoming year")

        elif ' can you do' in query:
            speak("I can oen some well known websites, extract information from wikipedia            Automate your google and more"
                  "but I am still in the procces of becoming more concise and effient ")
        elif 'what can you do for me' in query:
            speak("I can oen some well known websites, extract information from wikipedia            Automate your google and more"
                  "but I am still in the procces of becoming more concise and effient ")
        elif 'who made you' in query:
            speak("I am made, coded, desinged and developed by Mr.Avijit Singh")
            speak('if you want I can open his port folio websitr where you get all about him.')
            speak('Should I open it? yes or no')
        elif 'news' in query:
            speak('ok sir playing live news')
            speak('           analysing            best           news             live           now')
            webbrowser.open('https://youtu.be/u_DG4dDCMBQ')
            speak('analyze complete               ')
            speak('played live news on aaj tak')
        elif 'youtube history' in query:
            speak("Showing Avijit's youtube history")
            webbrowser.open('https://www.youtube.com/feed/history')
        elif 'okay quit now' in query:
            speak("okay sir have a good day!                             jarvis quiting")
            break
        elif 'okay jarvis quit now' in query:
            speak("okay sir have a good day!                             jarvis quiting")
            break
        elif ' jarvis quit now' in query:
            speak("okay sir have a good day!                             jarvis quiting")
        elif 'open Amazon ' in query:
            speak('wait')
            speak('opening your cart in amazon')
            webbrowser.open('https://www.amazon.com/ref=nosim?tag=msn015-20')
        # elif 'play music' in query:
        #     pass
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "my youtube playlist" in query:
            speak("OK sir, Here we go!")
            webbrowser.open('https://www.youtube.com/playlist?list=PLkjZS1KzvTGFusxQoLxYkpQNyIb5qFlZ0')
            speak("opening your your youtube playlist of alpha administrative account ")
        elif "what's going on" in query:
            speak('Nothing sir! Just going up with you!')
        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)

        elif " your name" in query:
            speak("My name is Jarvis which was given by Tony stalk")

        elif 'email to sir' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "avijitsingh2473@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")

        elif 'stop now' in query:
            speak("okay sir have a good day!                             jarvis quiting")
            break

