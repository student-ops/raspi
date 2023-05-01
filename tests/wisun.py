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


# cwd 引数を使って作業ディレクトリを変更


def read_data_from_serial():
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=work_dir)
    print(f"Current working directory: {os.getcwd()}")

    # 標準出力をリアルタイムで監視
    while True:
        output = process.stdout.readline()
        stripped_output = output.strip()
        if output == '' and process.poll() is not None:
            break
        if output:
            if "@" in stripped_output:
                numbers = extract_numbers(stripped_output)
                return numbers
        # エラー出力を確認
        stderr = process.stderr.read()
        if stderr:
            print(f"Goプログラムのエラー出力: {stderr.strip()}")


def send_post_request(url, data):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Status code {response.status_code}\n{response.text}")
        return None


def main():
    url = 'http://10.17.42.2:8080/handle'
    while True:
        try:
            numbers = read_data_from_serial()
            if (numbers == None or len(numbers) != 3):
                continue
            print(numbers)
            time.sleep(3)
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

            response = send_post_request(url, data)
            if response:
                print(response)
            else:
                print("POST request failed")
                break
        except KeyboardInterrupt:
            # Ctrl+Cが押された場合、サブプロセスを終了
            sys.exit()


if __name__ == "__main__":
    work_dir = "../go_serial"
    cmd = ["go", "run", "main.go"]
    main()
