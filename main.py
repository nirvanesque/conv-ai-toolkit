#!/usr/bin/env python3

# Import relevant libraries from Python packages
import speech_recognition as sr
import pyttsx3
#import pywhatkit
import datetime
import wikipedia
import pyjokes

#Initialise resources
listener = sr.Recognizer()
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
engine.setProperty('voice', voices[11].id)
engine.setProperty('rate', 180)
engine.say('Welcome to the conversational AI toolkit')

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    cmd = ''
    try:
        with sr.Microphone() as source:
            print('I am listening...')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'doctor' in cmd:
                cmd = cmd.replace('doctor', '')
                print(cmd)
    except:
        pass
    return cmd


def run_convai():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        #pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please repeat your command.')


while True:
    run_convai()
