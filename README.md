Use Redis as the message broker to handle the message queue functionality

**Installation**
1. Clone the repo to your local system

2. Once cloned, navigate inside the redismq folder and use the following command to install the library in your virtual environment `pip install .`.

3. Start the redis server and connect like below (if using localhost the command is `redis-server`).

**Usage**
1. Producer
```python
from redismq import Producer

r = Producer(host="localhost", port=6379, db=0)
key = "user1"
data = {
    "type": "page-view",
    "payload": {
        "user_id": "12345",
        "job_id": "67890",
        "timestamp": "2023-11-01T10:00:00Z",
    }
}

r.push(key, data)
```

2. Consumer
```python
from redismq import Consumer

consumer = Consumer(host="localhost", port=6379, db=0)
key = "user1"
print(consumer.len(key))
print(consumer.pop(key))
```

**Need to implement**
1. Batch processing
1. Error handling
1. Observability
