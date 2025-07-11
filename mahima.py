import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time

# --- Step 1: Initialize the Engine ONCE ---
# This 'engine' object will be used by the entire program.
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
except Exception as e:
    print("Error initializing text-to-speech engine. Please check your system's voice installations.")
    exit()

# --- Step 2: Define a CLEAN speak function ---
def speak(text):
    """
    This function takes text and makes Mahima speak it.
    It USES the engine we created at the start, it does NOT create a new one.
    """
    print(f"Mahima: {text}")
    engine.say(text)
    engine.runAndWait()

# --- Your other functions remain the same ---

def listen_for_command():
    """Listens for your voice command and returns it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return "None"

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-us').lower()
        # This first speak call will now work correctly
        speak(f"You said: {command}")
    except sr.UnknownValueError:
        speak("I'm sorry, I couldn't understand what you said.")
        return "None"
    except sr.RequestError:
        speak("I seem to be having trouble connecting to my speech service.")
        return "None"
    except Exception as e:
        print(e)
        return "None"
    return command

def wish_me():
    """Greets you when the program starts."""
    hour = int(datetime.datetime.now().hour)
    
    if 0 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
        
    full_message = f"{greeting} I am Mahima. How can I assist you today?"
    speak(full_message)

# --- Main Program Loop (Your excellent command list) ---

if __name__ == "__main__":
    wish_me()
    
    while True:
        command = listen_for_command()
        
        if command == "None":
            continue
        
        if 'hello' in command or 'hi' in command:
            speak("Hello! It's a pleasure to speak with you.")

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {strTime}")

        elif 'open youtube' in command:
            speak("Understood. Opening YouTube for you.")
            time.sleep(0.5) 
            webbrowser.open("https://youtube.com")

        elif 'open google' in command:
            speak("Of course. Opening Google.")
            time.sleep(0.5) 
            webbrowser.open("https://google.com")

        elif 'search for' in command:
            search_query = command.replace('search for', '').strip()
            speak(f"Right away. Searching Google for {search_query}")
            time.sleep(0.5) 
            webbrowser.open(f"https://google.com/search?q={search_query}")

        elif 'goodbye' in command or 'exit' in command or 'stop' in command: # Corrected 'good bye' to 'goodbye'
            speak("Goodbye! Have a wonderful day.")
            break
            
        elif 'open notepad' in command:
            speak("Opening Notepad.")
            os.system('notepad.exe')

        elif 'open calculator' in command:
            speak("Opening Calculator.")
            os.system('calc.exe')

        elif 'set alarm' in command:
            speak("At what time? Please say in HH:MM format.")
            alarm_time = listen_for_command()
            speak(f"Alarm set for {alarm_time}.")
            # This alarm logic will block the assistant, we can improve it later
            while True:
                if datetime.datetime.now().strftime("%H:%M") == alarm_time:
                    speak("Time to wake up!")
                    break
                time.sleep(10)

        elif 'play music' in command:
            # IMPORTANT: Make sure this path is correct for your system
            music_dir = 'E:/Songs'  
            try:
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing music.")
                else:
                    speak("No music files found in the directory.")
            except FileNotFoundError:
                speak(f"Sorry, I could not find the music directory at {music_dir}")

        elif 'take note' in command:
            speak("What should I write down?")
            note = listen_for_command()
            if note != "None":
                with open('notes.txt', 'a') as f:
                    f.write(f"- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {note}\n")
                speak("Note saved.")
            else:
                speak("I didn't catch the note. Please try again.")

        elif 'shutdown' in command:
            speak("Are you sure you want to shut down the system? Please say yes to confirm.")
            confirmation = listen_for_command()
            if 'yes' in confirmation:
                speak("Shutting down the system.")
                os.system('shutdown /s /t 5')
            else:
                speak("Shutdown cancelled.")

        elif 'restart' in command:
            speak("Are you sure you want to restart the system? Please say yes to confirm.")
            confirmation = listen_for_command()
            if 'yes' in confirmation:
                speak("Restarting the system.")
                os.system('shutdown /r /t 5')
            else:
                speak("Restart cancelled.")

        elif 'lock' in command:
            speak("Locking the system.")
            os.system('rundll32.exe user32.dll,LockWorkStation')

        else:
            speak("I'm sorry, but that is not a command I recognize yet. Please try another one.")