# main.py

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import asyncio
import json

app = FastAPI()

# ----------------------------------------------------
# 📌 1. CORSミドルウェアの設定（★file://からのアクセス許可★）
# ----------------------------------------------------
# すべてのオリジンからのアクセスを許可
origins = [
    "*", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------
# 📌 2. リアルタイム処理の中核: WebSocket エンドポイント
# ----------------------------------------------------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("クライアントが接続しました。")

    try:
        while True:
            # クライアントからメッセージ（JSON文字列）を受信
            data_str = await websocket.receive_text()
            
            try:
                # 💡 修正点：JSON文字列をPythonの辞書に変換
                data = json.loads(data_str)
            except json.JSONDecodeError:
                # JSON形式でない場合はスキップまたはエラー応答
                print(f"受信データがJSON形式ではありません: {data_str}")
                continue

            action = data.get("action", "talk")
            content = data.get("content", "発言")

            # --- AI処理のシミュレーション（クライアントからのアクションをそのまま返す） ---
            
            if action == "branch":
                response_json = {"action": "branch", "topic": content}
            elif action == "merge":
                # 💡 修正点：マージ操作時には、余計なtalkを返さない
                response_json = {"action": "merge"}
            else: # talk, またはその他のアクション
                response_json = {"action": "talk", "text": content}
            
            # AIの判定結果（Mermaid制御JSON）をクライアントに送信
            await websocket.send_text(json.dumps(response_json))
            
            await asyncio.sleep(0.05)

    except Exception as e:
        # クライアントが切断した場合もここに到達します
        print(f"接続エラーまたは切断: {e}")
    finally:
        print("クライアントが切断されました。")