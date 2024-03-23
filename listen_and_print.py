import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Calibrating microphone... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    print("Calibration is complete. Press Ctrl+C to stop.")

    try:
        while True:  # Continuous loop
            print("\nPlease speak now.")
            try:
                # Listening to the speech and capturing it for processing
                audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing...")
                try:
                    # Recognize speech using Google's speech recognition
                    text = recognizer.recognize_google(audio_data)
                    print("You said: " + text)
                except sr.UnknownValueError:
                    print("Sorry, I could not understand that.")
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                
    except KeyboardInterrupt:
        print("\nExiting...")
