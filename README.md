# Mahima AI

Mahima AI is a desktop voice assistant written in Python. The assistant is named after Mahima, who is my girlfriend.

## Features
- Voice-activated commands using speech recognition
- Greets you based on the time of day
- Tells the current time
- Opens YouTube and Google
- Performs Google searches
- Opens Notepad and Calculator
- Sets alarms
- Plays music from a specified folder
- Takes notes and saves them to a file
- Shuts down, restarts, or locks the system (with confirmation)
- Friendly fallback for unrecognized commands

## How to Use
1. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
   (You need `speechrecognition`, `pyttsx3`, and `pyaudio`.)

2. Run the assistant:
   ```sh
   python mahima.py
   ```

3. Speak your commands when prompted. Mahima will listen, respond, and perform actions for you!

## Notes
- The assistant uses your system's microphone and speakers.
- Make sure your music directory is set correctly in the code.
- Some features (like shutdown/restart) require appropriate system permissions.

## About the Name
Mahima is the name of my girlfriend, and this assistant is dedicated to her.

---

Enjoy using Mahima AI! 