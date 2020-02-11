import speech_recognition as sr

def get_txt_from_speech(language = "en-US"):
    """Get text from computer microphone using Google Speech Recognition."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        # For testing purposes, we're just using the default API key.
        # To use another API key, use
        # 'r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")'
        # instead of 'r.recognize_google(audio)'.
        print("Google Speech Recognition thinks you said '" + r.recognize_google(audio, language) + "'.")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    raw_text = r.recognize_google(audio, language)
    txt = raw_text if raw_text != None else None
    
    return txt