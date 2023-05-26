import os
import re
import requests
from dotenv import load_dotenv

def fetch_slack():
    load_dotenv()

    url = "https://slack.com/api/conversations.history"
    token = os.getenv('SLACK_BOT_OAUTH')

    header = {
        "Authorization": "Bearer {}".format(token)
    }

    payload = {
        "channel": "C0582MH6Y6M",
        "limit": 1
    }

    res = requests.get(url, headers=header, params=payload)
    response_data = res.json()

    if response_data["ok"]:
        messages = response_data["messages"]
        if messages:
            last_message = messages[0]
            message_text = last_message["text"]
            pattern = r"https[^>]*"
            print(message_text)
            result = re.findall(pattern, message_text)
            return result[0]
        else:
            print("No messages found in the channel.")
            return None
            
    else:
        print("Error: {}".format(response_data["error"]))
    return None
