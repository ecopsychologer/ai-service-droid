import speech_recognition as sr
import time

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Using try-except to catch the KeyboardInterrupt for a graceful exit
try:
    with sr.Microphone() as source:
        print("Calibrating microphone...")
        # Listen for 1 second and create the ambient noise energy level
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        while True:  # Loop to keep listening and processing
            print("\nGet ready to speak...")
            time.sleep(1)  # Wait a bit before listening
            print("Please speak now.")
            
            try:
                # Record audio until silence is detected, with slightly increased timeout and phrase_time_limit
                audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing...")
                
                # Recognize speech using Google's speech recognition
                text = recognizer.recognize_google(audio_data)
                print("You said: " + text)

                # Check if the user wants to exit
                if text.lower() == "exit":
                    print("Exiting...")
                    break

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

except KeyboardInterrupt:
    print("\nExiting...")  # Message to display when exiting the loop with Ctrl+C
