import pyttsx3


def speak(text):
    """Function to convert text to speech."""

    engine = pyttsx3.init('sapi5')  # Initialize the text-to-speech engine
    voices = engine.getProperty('voices')  # Get available voices
    print(voices)  # Print available voices for debugging
    engine.setProperty('voice', voices[0].id)  # Set the voice to the first available voice
    engine.setProperty('rate', 174)  # Set the speech rate
    # engine.setProperty('volume', 1)  # Set the volume to maximum (1
    engine.say(text)
    engine.runAndWait()

speak("I love you, Jarvis!")