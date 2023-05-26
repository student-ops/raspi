import subprocess
import os
import re
import time
from datetime import datetime
import requests
import json
import sys


def extract_numbers(output):
    # Extract numbers from the output using a regular expression
    number_strings = re.findall(r"[-+]?\d*\.\d+|\d+", output)
    # Convert the strings to float
    numbers = [float(num_str) for num_str in number_strings]
    return numbers


def send_post_request(numbers):
    headers = {
        'Content-Type': 'application/json'
    }
    print(numbers)
    now = datetime.utcnow()
    formatted_date = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    data = {
        "surroundings": [
            {
                "number": 1,
                "timestamp": formatted_date,
                "tempreture": numbers[0],
                "moisuture": numbers[1],
                "airPressure": numbers[2],
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
    first_line = True

    try:
        while True:
            output = process.stdout.readline()
            stripped_output = output.strip()
            print(f"output: {output}")
            if first_line:
                first_line = False
            if output:
                stripped_output = output.strip()
                print(stripped_output)
                if "@" in stripped_output:
                    numbers = extract_numbers(stripped_output)
                    send_post_request(numbers)
            # if error:
            #     print(f"Goプログラムのエラー出力: {error.strip()}")
            #     break

    except KeyboardInterrupt:
        # Ctrl+Cが押された場合、サブプロセスを終了
        sys.exit()


if __name__ == "__main__":
    work_dir = "../go_serial"
    cmd = ["go", "run", "main.go"]
    url = 'http://10.17.42.2:8080/handle'
    main()
