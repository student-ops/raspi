import sys
sys.path.append('../')

from post import json_to_audio
from aruduino_sync import tempreture
text = "今の気温は" + str(tempreture.readTemp) +"度です"
json_data = {
        "action": "speak",
        "speak" : {
            "speaker":1,
            "content":text
        }
}

print(json_to_audio.audioPost(json_data,"test"))
# playsound("../audio/test.wav")




