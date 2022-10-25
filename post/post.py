import requests

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}

json_data = {
    'action': 'voice',
    'content': 'hello from mac'
}
text  = 'hello from mac'
json_resp = None

response = requests.post('http://18.183.196.94:50021/audio_query?speaker=1', params ={"text": text, "speaker": 1} )

print(response)
