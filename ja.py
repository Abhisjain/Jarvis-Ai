
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int (datetime.datetime.now().hour)
    if  hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis speed 1 terahertz memory one settabyte Sir. Please tell me how may I help You")

def takeCommand():
    #takes microphone input and returns string output
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold= 350
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said :{query} \n")

    except Exception as e:
        print(e)  
        print("say that again please...")
        return "None"   
    return query

#   control + right mouse key for details      
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ajain3603@gmail.com', 'Abj@jain6')
    server.sendmail('ajain3603@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("Google.com")    
        elif 'open stackoverflow' in query:
            webbrowser.open("Stackoverflow.com") 
        elif 'open music' in query:     
            music_dir = 'C:\\Users\\Abhishek\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code ' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to abhishek ' in query:
            try:
                speak("What shoould i say")
                content = takeCommand()
                to = "ajain3603@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Abhishek. I am not able to sent this email!")