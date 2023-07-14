import random
import time
from queue import Queue
from threading import Thread

class EventProducer(Thread):

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            # Generate a random event
            event = {
                "user_id": random.randint(1, 100000),
                "event_type": random.choice(["access_app", "click_banner", "list_products", "select_product", "add_to_cart", "place_order"]),
                "timestamp": time.time(),
            }

            # Send the event to the queue
            self.queue.put(event)

            time.sleep(0.1)

class QueueConsumer(Thread):

    def __init__(self, queue, database):
        super().__init__()
        self.queue = queue
        self.database = database

    def run(self):
        while True:
            # Get an event from the queue
            event = self.queue.get()

            # Insert the event into the database
            self.database.insert(event)

            time.sleep(0.1)

def main():
    # Create a queue
    queue = Queue()

    # Create an event producer
    event_producer = EventProducer(queue)

    # Create a queue consumer
    queue_consumer = QueueConsumer(queue, database)

    # Start the event producer
    event_producer.start()

    # Start the queue consumer
    queue_consumer.start()

    # Wait for the event producer and queue consumer to finish
    event_producer.join()
    queue_consumer.join()

if __name__ == "__main__":
    main()



# This will start the event producer and queue consumer threads and wait for them to finish. Once the threads have finished, the code will exit