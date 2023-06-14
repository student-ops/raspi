import subprocess
import os
import re
import time
from datetime import datetime
import requests
import json
import sys
import fetch_slack

def extract_numbers(output):
    # Extract numbers from the output using a regular expression
    number_strings = re.findall(r"[-+]?\d*\.?\d+", output)
    # Convert the strings to float
    numbers = [float(num_str) for num_str in number_strings]
    return numbers


def send_post_request(numbers):
    headers = {
        'Content-Type': 'application/json'
    }
    # print(numbers)
    # path = "../data/gateway_data.txt"    
    # with open(path, mode='a') as f:
    #     for s in range(len(numbers)):
    #         f.write(str(numbers[s])+",")
    #     f.write("\n")
    now = datetime.utcnow()
    formatted_date = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    data = {
        "surroundings": [
            {
                "number": 1,
                "timestamp": formatted_date,
                "rssi": int(numbers[0]),
                "tempreture": numbers[1],
                "moisuture": numbers[2],
                "airPressure": numbers[3],
                
            },
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: Status code {response.status_code}\n{response.text}")
        return None


def main():
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=work_dir)
    print(f"Current working directory: {os.getcwd()}")

    # 検討
    try:
        while True:
            output = process.stdout.readline()
            stripped_output = output.strip()
            print(f"output: {output}")
            if output:
                stripped_output = output.strip()
                print(stripped_output)
                if "@" in stripped_output:
                    numbers = extract_numbers(stripped_output)
                    send_post_request(numbers)

    except KeyboardInterrupt:
        # Ctrl+Cが押された場合、サブプロセスを終了
        sys.exit()


if __name__ == "__main__":
    
    work_dir = "../go_serial/gateway"
    cmd = ["go", "run", "main.go"]
    args = sys.argv
    url = fetch_slack.fetch_slack()
    url = url + "/handle"
    print(url)
    main()
