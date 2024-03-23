import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Set up the microphone
with sr.Microphone(device_index=2) as source:  # Change device_index based on your microphone
    print("Listening...")
    while True:
        # Adjust the recognizer sensitivity to ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio_data = recognizer.listen(source)
        print("Processing...")
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said: {}".format(text))
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))
