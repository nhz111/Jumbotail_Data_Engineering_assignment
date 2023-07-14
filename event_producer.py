
import threading
import random
import time

class DRIVER(threading.Thread):
    def __init__(self, num_users):
        self.num_users = num_users
        self.events = []

    def generate_events(self):
        for _ in range(self.num_users):
            user_id = random.randint(1, 100000)
            city = random.choice(["New delhi", "banglore", "pune", "mumbai"])
            events = []
            for event_type in ["access_app", "click_banner", "view_products", "add_to_cart", "place_order"]:
                if random.random() < 0.5:
                    events.append({"event_type": event_type, "user_id": user_id, "city": city})
            self.events.extend(events)

    def send_events(self):
        for batch in self.events:
            response = requests.post("localhost:8888/webhook", json=batch)
            time.sleep(0.1)

if __name__ == "__main__":
    DRIVER(10000).generate_events().send_events()