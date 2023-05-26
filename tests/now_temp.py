import sys
sys.path.append('../src')

from post import json_to_audio
from aruduino_sync import tempreture
from playsound import playsound

if __name__ == '__main__':
  temp = str(tempreture.readTemp())
  text = "今の気温は" + temp +"℃です"
  print(text)
  json_data = {
          "action": "speak",
          "speak" : {
              "speaker":1,
              "content":text
          }
  }
  if(json_to_audio.audioPost(json_data,"temp")):
    playsound("../audio/temp.wav")




