from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "SSHX is running!"

def run():
    # Render cung cấp biến môi trường PORT, nếu không có thì dùng 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():  
    t = Thread(target=run)
    t.start()
