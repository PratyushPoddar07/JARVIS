import os

import eel

eel.init("www") # to recognize our frontend directory

os.system('start msedge.exe --app="http://localhost:8000/index.html"') # to open the browser
eel.start("index.html",mode="none",host="localhost",block=True) # to start the eel application