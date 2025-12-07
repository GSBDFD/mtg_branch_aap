#!/bin/bash

# 仮想環境 (venv) の構築
echo "--- 1. 仮想環境を構築します ---"
python3 -m venv venv

# 仮想環境の有効化
echo "--- 2. 仮想環境を有効化します ---"
source venv/bin/activate

# 依存関係のインストール
echo "--- 3. 依存関係をインストールします ---"
python3 -m pip install -r requirements.txt

echo "--- ✅ 環境構築が完了しました！ ---"
echo "次のステップ: source venv/bin/activate で環境を有効化し、uvicorn main:app --port 8002 でサーバーを起動してください。"

# スクリプト実行後も環境が有効化され続けるように、有効化コマンドを再度プロンプトに出力
source venv/bin/activate