# Jarvis AI Assistant 🤖

A voice-controlled AI assistant built with Python, Google Gemini, and NewsAPI.

## Features
- 🎙️ Voice commands with "Jarvis"
- 🌐 Open websites (Google, Facebook, YouTube, LinkedIn)
- 🎵 Play music on YouTube
- 📰 Fetch top news headlines (India/US)
- 💬 Conversational AI with Google Gemini

## Requirements
- Python 3.13+
- `google-genai`, `speech_recognition`, `gTTS`, `pygame`, `yt_dlp`, `python-dotenv`
- Gemini API key & NewsAPI key

## Setup
1. Clone: `git clone https://github.com/yourusername/Jarvis-AI-Assistant`
2. Install: `pip install -r requirements.txt`
3. Add `.env` with `GEMINI_API_KEY` and `NEWS_API_KEY`
4. Run: `python main.py`

## Usage
- Say "Jarvis" to activate
- Commands:
  - "Open Google"
  - "Play <song>"
  - "News"
  - "What's the weather?" (via Gemini AI)

## Code Structure
- `main.py`: Core logic
- `.env`: API keys

## API Keys
Get keys from [Gemini](https://gemini.google.com/) & [NewsAPI](https://newsapi.org/).
