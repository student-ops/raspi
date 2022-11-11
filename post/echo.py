import requests
# from playsound import playsound
import json
# from os import chdir
json_data = {
        "action": "echo"
}

url ='http://18.183.196.94/handle'
# url ='http://localhost:8080/handle'
# url = 'http://localhost:8080/speak'
header = {'Content-Type':'application/json'}
d = json.dumps(json_data)
print(d)
response = requests.post(url,headers = header,data=d)
# response = requests.post(url,headers = header)
if response.status_code == 200:
    print("accepted")
    f = open("audio3.wav","wb")
    f.write(response.content)
    f.close()
    # chdir("/Users/lakky/raspy/post")
    # playsound("audio3.wav")
else:
    print("error respose\n")
    content = json.loads(response.content)
    print(content)



