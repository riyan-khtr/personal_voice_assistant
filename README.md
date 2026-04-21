Personal Voice Assistant (Python)
A smart desktop voice assistant built with Python that can listen to your voice, 
understand commands, and perform tasks like opening apps, searching the web,
playing YouTube, telling time, and fetching information from Wikipedia.


Features
 Speech-to-Text using SpeechRecognition
 Text-to-Speech using pyttsx3
 Google search in browser
 YouTube search and play
 Wikipedia summaries via Wikipedia
 Open desktop apps (Notepad, Calculator, Paint, Chrome, VS Code, Explorer)
 Tell current time
 Exit by voice command


## Technologies Used
Python
SpeechRecognition
pyttsx3
wikipedia
OS / Webbrowser modules


## Installation

Install required packages:

pip install SpeechRecognition pyttsx3 wikipedia pyaudio

If pyaudio fails on Windows:

pip install pipwin
pipwin install pyaudio


## How to Run
python voice.py

Wait 1 second, then speak your command clearly.

 Example Voice Commands
“Open notepad”
“Open chrome”
“Open vscode”
“Search Python tutorials”
“YouTube lofi music”
“Wikipedia Albert Einstein”
“What is the time”
“Exit”
