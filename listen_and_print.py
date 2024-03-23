import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# No need to specify device_index for default microphone
with sr.Microphone() as source:
    print("Calibrating microphone...")
    # Listen for 1 second and create the ambient noise energy level
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Please speak now.")
    
    try:
        # Record audio until silence is detected
        audio_data = recognizer.listen(source)
        print("Processing...")

        # Recognize speech using Google's speech recognition
        text = recognizer.recognize_google(audio_data)
        print("You said: " + text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

