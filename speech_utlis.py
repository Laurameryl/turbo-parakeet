import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def transcribe_speech(language="en-US"):
    """Transcribes speech from the microphone into text."""
    with microphone as source:
        print("🎙️ Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        return "⚠️ Could not understand audio"
    except sr.RequestError:
        return "⚠️ API unavailable"
