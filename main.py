from redismq import Producer, Consumer


producer = Producer(host="localhost", port=6379, db=0)
key = "user1"
data = {
    "type": "page-view",
    "payload": {
        "user_id": "12345",
        "job_id": "67890",
        "timestamp": "2023-11-01T10:00:00Z",
    }
}
producer.push(key, data)
print(producer.len(key))


consumer = Consumer(host="localhost", port=6379, db=0)
key = "user1"
print(consumer.len(key))
print(consumer.pop(key))