import sys
sys.path.append('../')

from post import json_to_audio
from aruduino_sync import tempreture
temp = str(tempreture.readTemp)
text = "今の気温は" + temp +"度です"
print(text)
json_data = {
        "action": "speak",
        "speak" : {
            "speaker":1,
            "content":text
        }
}

print(json_to_audio.audioPost(json_data,"test"))
# playsound("../audio/test.wav")




