python サブプロセスを使用し go を実行、出力をリアルタイムでうけとる
a.py

```a.py
import subprocess

# Goプログラムをサブプロセスとして実行
cmd = ["go", "run", "b.go"]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 標準出力をリアルタイムで監視
try:
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(f"Goプログラムの出力: {output.strip()}")

    # エラー出力を確認
    stderr = process.stderr.read()
    if stderr:
        print(f"Goプログラムのエラー出力: {stderr.strip()}")

except KeyboardInterrupt:
    # Ctrl+Cが押された場合、サブプロセスを終了
    process.terminate()
```

b.go

```b.go
package main

import (
	"fmt"
	"time"
)

func test() string {
	for {
		fmt.Println("hello")
		time.Sleep(5 * time.Second)
	}
}


```
