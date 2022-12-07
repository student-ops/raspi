import sys
sys.path.append('../')

from post import json_to_audio
from aruduino_sync import read_tempreture
text = "今の気温は" + str(read_tempreture.readTempreture) +"度です"
json_data = {
        "action": "speak",
        "speak" : {
            "speaker":1,
            "content":text
        }
}

print(json_to_audio.audioPost(json_data,"test"))
# playsound("../audio/test.wav")




