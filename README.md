# 🩺 Voice-Activated Healthcare Chatbot

A voice-interactive medical assistant powered by **OpenAI GPT-4**, designed to help users inquire about symptoms, health topics, and interact through natural speech.

---

## 🚀 Features

- 🎙️ Voice Input using SpeechRecognition
- 🔊 Voice Output using pyttsx3
- 🧠 Medical Q&A via OpenAI GPT-4
- 📊 COVID-19 data via public API
- 🧾 Health topic lookup (WebMD placeholder)

---

## 📦 Tech Stack

- Python 3.7+
- OpenAI API
- Libraries:
  - `openai`
  - `requests`
  - `speechrecognition`
  - `pyttsx3`
  - `pyaudio`

---

## 📋 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/healthcare-chatbot.git
cd healthcare-chatbot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

If `pyaudio` causes issues on Windows, install it using a `.whl` from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

---

## 🔑 Configuration

1. Replace your OpenAI API key in the script:

```python
OPENAI_API_KEY = "your-api-key-here"
```

---

## ▶️ Usage

Run the chatbot:

```bash
python chatbot.py
```

Speak into your microphone to interact. Example commands:

- "I have a sore throat"
- "Give me health info about diabetes"
- "Talk to GPT"
- "Exit" or "Bye"

---

## ⚠️ Disclaimer

This chatbot is for **educational purposes only** and not intended for medical diagnosis or treatment. Please consult a licensed medical professional for health concerns.

---

## 📄 License

This project is licensed under the MIT License.
