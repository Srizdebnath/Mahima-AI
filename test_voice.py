import pyttsx3

# Initialize the voice engine
engine = pyttsx3.init() 

# Test Line 1
print("Testing the voice engine...")
engine.say("Hello, can you hear me? This is a test.")
engine.runAndWait()

# Test Line 2
print("If you heard the first line, this should work too.")
engine.say("Test number two is complete.")
engine.runAndWait()

print("Test finished.")