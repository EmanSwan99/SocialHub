
# bot.py
import time

def check_messages():
    # Placeholder for Instagram API later
    print("Checking for new messages...")

def send_message(user_id, text):
    # Placeholder for sending message
    print(f"Would send to {user_id}: {text}")

# Main loop
if __name__ == "__main__":
    while True:
        check_messages()
        # Example: auto-response simulation
        send_message("demo_user", "Hey! Thanks for reaching out.")
        time.sleep(60)  # wait 60 seconds before repeating
