import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import google.genai as genai
from gtts import gTTS
import pygame
from yt_dlp import YoutubeDL
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def init_gemini():
    print("Gemini initialized")

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    system_instruction = (
        "You are a virtual assistant named Jarvis, skilled in general "
        "tasks like Alexa and Google Cloud. Give short responses please."
    )
    try:
        model = genai.GenerativeModel("gemini-2.0-flash", api_key=GEMINI_API_KEY)
        response = model.generate_content(f"{system_instruction}\n\nUser: {command}")
        return response.text
    except Exception as e:
        return f"Error: {e}"

def play_on_youtube(query):
    speak(f"Playing {query}")
    ydl_opts = {"quiet": True, "default_search": "ytsearch1"}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        video = info["entries"][0]
        webbrowser.open(video["webpage_url"])

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        query = c[5:].strip()
        if query:
            play_on_youtube(query)
        else:
            speak("What would you like me to play?")
    elif "news" in c.lower():
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?q=india&apiKey={NEWS_API_KEY}"
        )
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if not articles:
                speak("No news articles found right now.")
                return
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Sorry, I could not fetch the news right now.")
    else:
        output = aiProcess(c)
        speak(output)

def init_gemini():
    print("Gemini initialized")

def aiProcess(command):
    system_instruction = (
        "You are a virtual assistant named Jarvis, skilled in general "
        "tasks like Alexa and Google Cloud. Give short responses please."
    )
    try:
        model = genai.GenerativeModel("gemini-2.0-flash", api_key=GEMINI_API_KEY)
        response = model.generate_content(f"{system_instruction}\n\nUser: {command}")
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    init_gemini()
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Ya")
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)
        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            continue
        except Exception as e:
            print("Error: {0}".format(e))