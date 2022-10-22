import requests

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}

json_data = {
    'voice': 'こんにちは',
}

response = requests.post('http://18.183.196.94:8080/json', headers=headers, json=json_data)