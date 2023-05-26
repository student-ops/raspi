import sys
from pathlib import Path

sys.path.append('../')

sys.path.append(str(Path(__file__).resolve().parent.parent))
from post import json_to_audio
from playsound import playsound

if __name__ == '__main__':
  args = sys.argv
  if(args[1] == "local"):
    local = True
    url = "http://localhost:8080/handle"


  json_data = {
          "action": "echo",
  }
  if(json_to_audio.audioPost(json_data,"echo",url)):
    if(local != True):
      playsound("../audio/echo.wav")


