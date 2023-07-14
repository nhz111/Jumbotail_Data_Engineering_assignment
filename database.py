import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("events.db")

    def insert_event(self, event):
        c = self.connection.cursor()
        c.execute("INSERT INTO events (event_type, user_id, city) VALUES (?, ?, ?)", (event["event_type"], event["user_id"], event["city"]))
        self.connection.commit()