import requests
import json

json_data = {
    "action": "echo"
}

# url ='http://18.183.196.94:50021/handle'
header = {'Content-Type':'application/json'}
url ='http://localhost:8081/handle'
d = json.dumps(json_data)
response = requests.post(url,headers = header,data=d)
print("respose status "+str(response.status_code))
f = open("audio2.wav","wb")
f.write(response.content)
f.close()
# playsound(audio2.wav)




