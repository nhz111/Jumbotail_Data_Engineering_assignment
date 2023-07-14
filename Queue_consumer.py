import threading
import random

def event_consumer(queue):
    while True:
        event = queue.get()
        if event is None:
            break

        # Insert the event into the database
        try:
            event_repository.insert(event)
        except Exception as e:
            # Re-insert the event
            time.sleep(random.randint(1, 10))
            queue.put(event)

if __name__ == "__main__":
    queue = Queue()
    event_consumer(queue)

