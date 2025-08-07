import pyttsx3
import speech_recognition as sr

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

def takecommand():
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Listening...")
        r.pause_threshold = 1  # Set the pause threshold for recognizing speech
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)  # Listen for audio input

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognize speech using Google Web Speech API
        print(f"User said: {query}\n")  # Print the recognized text
    except Exception as e:
        print("Sorry, I did not understand that. Please try again.")
        return "None"  # Return None if speech recognition fails
    
    return query.lower()  # Return the recognized text

text = takecommand()  # Call the function to take command from the user

speak(text)