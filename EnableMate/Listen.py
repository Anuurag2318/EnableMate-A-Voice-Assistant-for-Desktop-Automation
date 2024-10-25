import speech_recognition as sr
from Speak import speak

def Listen(timeout=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        try:
            audio = r.listen(source, timeout=timeout)
            print("recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
            return str(query).lower()

        except sr.UnknownValueError:
            speak("Please repeat...")
            return Listen(timeout) 

        except sr.RequestError as e:
            print(f"Error with the request to Google Speech Recognition service: {e}")
            speak("There was an error. Please try again.")
            return None 