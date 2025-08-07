from playsound import playsound
import eel
# playing jarvis assistant sound
@eel.expose
def playAssistantsound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)