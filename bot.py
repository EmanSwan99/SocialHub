import time
import datetime

def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now}  {msg}", flush=True)  # flush so logs show up immediately

if __name__ == "__main__":
    log("Booted SocialHub worker.")
    while True:
        log("Heartbeat: worker is alive.")
        time.sleep(10)

