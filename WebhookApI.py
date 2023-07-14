import requests
import random

def event_webhook(event):
    webhook_url = "http://localhost:8888/webhook"
    try:
        requests.post(webhook_url, json=event)
    except Exception as e:
        # Re-send the event
        time.sleep(random.randint(1, 10))
        requests.post(webhook_url, json=event)

if __name__ == "__main__":
    event = {
        "user_id": "123456",
        "event_name": "event_name",
        "timestamp": int(time.time()),
    }
    event_webhook(event)

