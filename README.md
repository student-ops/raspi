## clone branch

## activate venv
ptest デイレクトリには入らす。

`. ptest/bin/activate`

hello good after noon


# Github コマンド チートシート

基本
```
branch -a ブランチ一覧
checkout <branch name>ブランチの切り替え
checkout -b <branc name> ブランチの作成 & 切り替え
push <origin> <branch>
pull <origin> <branch>
rmeote -a リモートとして登録されているものを一覧する
```

作業開始前の更新 & 確認

```

git fetch --all 
git pull origin <branch name>
git branch -a
```

リモートブランチをローカルに持ってくる
```
// ローカルの更新
git fetch --all 
git pull

//リモートをローカルにコピー
git checkout -b <コピーするローカルブランチ名> <origin>/<リモートブランチ名>
```

ローカルブランチをリモートにpush
```
git push -u <origin> <localBranch>
```

## python /tests/ ファイル名
wisun通信無しでprint -> request : wisun.py<br>
wisun通信受信 -> request :wisun_receive.py<br>
wisun通信送信 : wisun_send.sh<br>

wisun_send.py