import sys
sys.path.append('../')

from post import json_to_audio
# from playsound import playsound

if __name__ == '__main__':
  temp = "12"
  text = "今の気温は" + temp +"℃です"
  url = "http://10.17.42.2/handle"
  print(text)
  json_data = {
          "action": "speak",
          "speak" : {
              "speaker":1,
              "content":text
          }
  }
  json_to_audio.audioPost(json_data,"temp",url)
    # playsound("../audio/temp.wav")
