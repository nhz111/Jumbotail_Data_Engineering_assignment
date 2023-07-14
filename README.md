# Jumbotail_Data_Engineering_assignment
The task at hand pertains to the development of a system for tracking user journey within an e-commerce application.

Event Producer:

-Create a DRIVER class that uses multithreading to generate events for each user.
-The DRIVER class will generate events for each user, with each event representing a particular step of the funnel and containing information related to it.
-The generateEvent() method should consider user behavior when generating events. This means generating events in a ratio that reflects the actual user behavior, considering the order of events, which events are more frequent, which stages users engage with the most, and at which stages users are more likely to drop out.
-The generateEvent() method should also implement batching when sending events. This helps in optimizing the process by sending events in batches rather than sending them individually.
-The generateEvent() method should also consider how the Event entity will be structured to answer the questions required in the Final Output. This means designing the Event entity in a way that allows extracting the necessary information to generate the desired output.
-The generateEvent() method should also log the response time of the API calls. It is expected that the response time will be in the order of milliseconds.
The DRIVER class should invoke the eventWebhook() method to send the events to the webhook API.
- we used "event_producer.py"

Webhook:

-Implement a REST API that can be accessed at localhost:8888/webhook.
-The API should process requests asynchronously by utilizing an in-memory queue.
- we use here "webhook.py"

In-memory queue:

-Select an in-memory queue system.
-The main objective of the queue is to enable asynchronous behavior.
-Events will be pushed into the in-memory queue, and a consumer will retrieve the events from the queue to ultimately insert them into a database of your preference.
- we use here "in_memory.py"
Queue Consumer:

-The queue consumer is responsible for retrieving messages from the in-memory queue in batches and inserting them into the database of your choice.
-The queue consumer should process multiple messages together for efficient handling.
-The queue consumer should implement a retrial mechanism in case there are failures during the database insertion process.
-The queue consumer should handle duplicate events coming from the client.
-we use here "Queue_consumer.py"

Database:
-The database will be used to store the events and generate the required output as described in the Final Output section.
-The database should be able to handle multiple asynchronous write requests.
-we use here "database.py"

-Once the solution is implemented, the final output should include the following information:

Percentage of users in each stage of the user journey.
Evaluation of the performance of different cities.
-we use here "percentage_of_user_stagewise.sql"
-and "percentage_of_user_citywise.sql"

Requirements:
Python 3.6+
Pip
Requests
SQLite3

Installation:
Install the necessary dependencies.
-The API should implement a retrial mechanism in case push operation to the queue fails.
