import subprocess
import os

def main():
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=work_dir)
    print(f"Current working directory: {os.getcwd()}")

    # 実行結果を取得
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        # 成功した場合の処理
        print("コマンドの実行に成功しました。")
        print("標準出力:")
        print(stdout)
    else:
        # エラーが発生した場合の処理
        print("コマンドの実行に失敗しました。")
        print("標準エラー出力:")
        print(stderr)

if __name__ == "__main__":
    work_dir = "../go_serial/vuoy/"
    cmd = ["go", "run", "main.go"]
    main()