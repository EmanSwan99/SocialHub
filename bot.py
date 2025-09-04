import time
import threading
import datetime
from flask import Flask

app = Flask(__name__)

def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now}  {msg}", flush=True)  # flush ensures logs show up in Render

def background_loop():
    log("Background worker started.")
    while True:
        log("Heartbeat: worker is alive.")
        time.sleep(10)

# Start background loop in a separate thread
threading.Thread(target=background_loop, daemon=True).start()

@app.route("/")
def home():
    return "SocialHub bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
