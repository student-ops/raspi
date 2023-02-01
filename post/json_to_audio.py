import requests
# from playsound import playsound
import json
# from os import chdir
def audioPost(json_data,file_name,url):
    header = {'Content-Type':'application/json'}
    d = json.dumps(json_data)
    response = requests.post(url,headers = header,data=d)
    if response.status_code == 200:
        dest = "../audio/" + file_name + ".wav"
        f = open(dest,"wb")
        f.write(response.content)
        f.close()
        return True
    else:
        return False



