import os
import re
import requests
from dotenv import load_dotenv


def fetch_slack():
    channelid = "C0591HUR5RQ"
    load_dotenv()
    token = os.environ["SLACK_BOT_OAUTH"]

    url = "https://slack.com/api/conversations.history"

    header = {
        "Authorization": "Bearer {}".format(token)
    }

    payload = {
        "channel": channelid,
        "limit": 1
    }

    res = requests.get(url, headers=header, params=payload)
    response_data = res.json()

    if response_data["ok"]:
        messages = response_data["messages"]
        if messages:
            last_message = messages[0]
            message_text = last_message["text"]

            # print(message_text)
            pattern = "<(https?://[^>]*)"

            result = re.findall(pattern, message_text)
            print(result)
            return result[0]
        else:
            print("No messages found in the channel.")
            return None
            
    else:
        print("Error: {}".format(response_data["error"]))
    return None


if __name__ == "__main__":
    a = fetch_slack()
    print(a)