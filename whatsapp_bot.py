from flask import Flask, request
import requests
from bot import get_attendance   # ← imports your existing file

# ===== GREEN API =====
ID_INSTANCE = "7103531355"
API_TOKEN = "99d7d35848a542fbb5040f9e3965c9e4f10a9137d7d443f38b"

SEND_URL = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN}"

app = Flask(__name__)

def send_whatsapp(chat_id, text):
    data = {"chatId": chat_id, "message": text}
    requests.post(SEND_URL, json=data)

@app.route("/", methods=["POST"])
@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print(data)

    try:
        if data.get("typeWebhook") == "incomingMessageReceived":
            msg = data["messageData"]["textMessageData"]["textMessage"]
            chat = data["senderData"]["chatId"]

            if "attendance" in msg.lower():
                percent = get_attendance()
                send_whatsapp(chat, f"Your attendance is {percent}%")

    except Exception as e:
        print("Error:", e)

    return "ok"

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

