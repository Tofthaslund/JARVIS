import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text

USERNAME = config("USER")
BOTNAME = config("BOTNAME")


engine = pyttsx3.init('sapi5')

# set rate
engine.setProperty('rate', 190)

# set Volume
engine.setProperty('volume', 1.0)

# set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# text to speech conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


def greet_user():
    """Greets the user accoring to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USERNAME}")
    speak(f"How am {BOTNAME}. How may I assist you")


def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and coverts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()
    except Exception:
        speak("Sorry, I did not understand. Could you please say it again")
        query = 'None'
    return query