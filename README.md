# mtg_branch_aap
create mtg branch app

install.shを実行するには以下のコマンドを使用
chmod +x install.sh
./install.sh

サーバについて
lsof -i :8002でサーバ立ってるか確認

kill -9 PID　でサーバを閉じる

uvicorn main:app --port 8002　で再度サーバ立てる