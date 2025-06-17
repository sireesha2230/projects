import requests
import openai
import speech_recognition as sr
import pyttsx3
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your openAPI-key)
SYMPTOM_API_URL = "https://disease.sh/v3/covid-19/countries"
openai.api_key = OPENAI_API_KEY
engine = pyttsx3.init()
engine.setProperty("rate", 150)
recognizer = sr.Recognizer()
def speak(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
def fetch_symptom_data():
    try:
        response = requests.get(SYMPTOM_API_URL)
        if response.status_code == 200:
            data = response.json()
            top3 = sorted(data, key=lambda x: x.get("cases", 0), reverse=True)[:3]
            info = ", ".join([f"{c['country']} has {c['cases']} cases" for c in top3])
            return f"Top affected countries: {info}."
        else:
            return "Couldn't fetch health data."
    except:
        return "Error retrieving symptom information."
def fetch_health_article(query):
    return f"Here is a WebMD article about {query}. Please visit webmd.com for more details."
def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Failed to contact GPT-4."
def chatbot():
    speak("Hello! I am your healthcare assistant. How can I help you today?")

    while True:
        user_input = listen()

        if not user_input:
            speak("Sorry, I didn't catch that. Please try again.")
            continue

        if "symptom" in user_input or "covid" in user_input:
            speak("Checking health statistics for COVID-19.")
            info = fetch_symptom_data()
            speak(info)

        elif "health info" in user_input or "webmd" in user_input:
            speak("What topic do you want health information about?")
            topic = listen()
            article = fetch_health_article(topic)
            speak(article)

        elif "gpt" in user_input or "talk to doctor" in user_input:
            speak("Please describe your medical question.")
            question = listen()
            answer = get_gpt_response(question)
            speak(answer)

        elif "exit" in user_input or "quit" in user_input or "bye" in user_input:
            speak("Goodbye! Stay safe and healthy.")
            break

        else:
            speak("I'm here to help with health questions. You can ask about symptoms, health info, or talk to GPT.")


if __name__ == "__main__":
    chatbot()
