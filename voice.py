import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
import sys
import subprocess

# ---------------- TTS (Text To Speech) ----------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- STT (Speech To Text) ----------------
def listen():
    r = sr.Recognizer()
    r.energy_threshold = 350
    r.pause_threshold = 0.7

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.8)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            text = r.recognize_google(audio, language="en-IN").lower()
            print("You said:", text)
            return text

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            speak("Internet issue.")
            return ""

# ---------------- ACTIONS ----------------
def open_app(app):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "vscode": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "explorer": "explorer.exe"
    }

    if app in apps:
        try:
            subprocess.Popen(apps[app])
            speak(f"Opening {app}")
        except:
            speak(f"Cannot open {app}")
    else:
        speak("Application not configured.")

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")

def open_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    speak(f"Playing {query} on YouTube")

def wiki_search(topic):
    try:
        result = wikipedia.summary(topic, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("Topic is too broad. Please be more specific.")
    except:
        speak("I could not find information on Wikipedia.")

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

# ---------------- COMMAND HANDLER ----------------
def handle_command(text):
    if not text:
        return

    if "time" in text:
        tell_time()

    elif "open notepad" in text:
        open_app("notepad")

    elif "open calculator" in text:
        open_app("calculator")

    elif "open paint" in text:
        open_app("paint")

    elif "open chrome" in text:
        open_app("chrome")

    elif "open vscode" in text or "open code" in text:
        open_app("vscode")

    elif "open explorer" in text or "open files" in text:
        open_app("explorer")

    elif "youtube" in text:
        query = text.replace("youtube", "").strip()
        open_youtube(query)

    elif "search" in text:
        query = text.replace("search", "").strip()
        search_google(query)

    elif "wikipedia" in text:
        topic = text.replace("wikipedia", "").strip()
        wiki_search(topic)

    elif "stop" in text or "exit" in text or "quit" in text:
        speak("Goodbye! Have a nice day.")
        sys.exit(0)

# ---------------- MAIN LOOP ----------------
def main():
    speak("Hello. I am your personal voice assistant. How can I help you?")
    while True:
        command = listen()
        handle_command(command)

if __name__ == "__main__":
    main()