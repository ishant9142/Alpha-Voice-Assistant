import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello sir I am Alpha always ready for your service. How may I help you ?")       

def order():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening...")
        
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:
          
        print("please say that again")  
        return "None"
    return command

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anonymousguy759@gmail.com', '12345678c#')
    server.sendmail('anonymousguy759@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    greet()
    while True:
   
        command = order().lower()

        
        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            speak("opening youtube sir")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("opening google sir")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com")   

        

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        
        elif 'email' in command:
            try:
                speak("Start dictating me your email sir")
                content = order()
                to = input("Enter the email id of receiver: ")   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am really very sorry sir the mail was not sent.")  
        elif 'mail' in command:
            try:
                speak("Start dictating me your email sir")
                content = order()
                to = input("Enter the email id of receiver: ")   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am really very sorry sir the mail was not sent.")  
        elif 'whatsapp'  in command:
            speak("Opening whats app sir")
            webbrowser.open("web.whatsapp.com")
        elif  'music' in command:
            music_dir = 'C:\\Users\\rahul_qmiywj7\\Desktop\\songs'
            speak("Playing your playlist sir")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        elif  'song' in command:
            music_dir = 'C:\\Users\\rahul_qmiywj7\\Desktop\\songs'
            speak("Playing your playlist sir")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        elif 'bye' in command:
            speak ("Good Bye sir and have a nice day")
            quit()
        elif 'how are you' in command:
            speak("I AM FINE SIR, how are you..?")
        elif 'good' in command:
            speak("good to hear that sir!!")
        elif 'fine' in command:
            speak("good to hear that sir!!")
        
        
        elif 'turn off' in command:
            speak("do you really want to turn off sir?")
            reply = order()
            if 'yes' in reply:
                speak("Turning off your laptop sir, go take some rest and have a nice day sir, good bye")
                os.system("shutdown /s /t 1")
            else:
                speak("As you wish sir")
        elif 'shutdown' in command:
            speak("do you really want to turn off sir?")
            reply = order()
            if 'yes' in reply:
                speak("Turning off your laptop sir, go take some rest and have a nice day sir, good bye")
                os.system("shutdown /s /t 1")
            else:
                speak("As you wish sir")
            
        elif 'open class' in command:
            speak("Opening your class sir")
            webbrowser.open('https://cuchd.blackboard.com/ultra/course')
        elif 'restart' in command:
            speak("Do you really want to restart sir?")
            reply = order()
            if 'yes' in reply:
                speak("Restarting your system sir, will be right back")
                os.system("shutdown /r /t 1")
            else:
                speak("As you wish sir")

