import queue

class InMemoryQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def push(self, event):
        self.queue.put(event)

    def pop(self):
        return self.queue.get()