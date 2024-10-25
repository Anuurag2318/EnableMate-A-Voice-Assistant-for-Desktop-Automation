# import pyttsx3
import datetime
from Speak import speak

def greetMe():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak(f"Good Morning! It's {current_time}.")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon! It's {current_time}.")
    else:
        speak(f"Good Evening! It's {current_time}.")

    speak("Hello Sir, I am EnableMate. How can I help you?")
