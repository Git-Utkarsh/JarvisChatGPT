import openai
import pyttsx3
import speech_recognition as sr
openai.api_key = "<OPENAI API Key>"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.75
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("====================================================================================================================================================================================")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query
messages = []
messages.append({"role": "system", "content": "ChatGPT"})
mess = "greet me"
messages.append({"role": "user", "content": mess})
response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
reply = response["choices"][0]["message"]["content"]
messages.append({"role": "assistant", "content": reply})
speak(reply)
while input != "quit()":
    message = takeCommand()
    if message == "goodbye":
        exit()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("====================================================================================================================================================================================\nGPT : " + reply + "\n" + "====================================================================================================================================================================================")
    speak(reply)
