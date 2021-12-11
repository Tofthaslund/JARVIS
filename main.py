import pyttsx3
from decouple import config
from datetime import datetime

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