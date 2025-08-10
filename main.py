import os

import eel

from engine.features import *
from engine.command import *
eel.init("www") # to recognize our frontend directory

playAssistantsound() # to play the assistant sound
os.system('start msedge.exe --app="http://localhost:8000/index.html"') # to open the browser
eel.start("index.html",mode="none",host="localhost",block=True) # to start the eel application


# install 
# pip install Eel
# pip install pywhatkit