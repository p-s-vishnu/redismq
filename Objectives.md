**Overview**
1. Send events from Django website
    - 10k req per day
    - 1 page per job
2. Analytics
    - Event log architecture: page view + extra info (like: candidate profile info) saved
    - many other events exist (search, conversions, etc)

**Requirements**
- A python message queue on redis
- Easy to use for the producer and the consumer
- Distributed processing

**Extra info**
- Batch processing will help
- Reduced latency
- Variable user activity
- Error handling
- Observability (both producer and consumer)
- JSON format data
Example message format:
   ```json
   {
     "type": "page-view",
     "payload": {
       "user_id": "12345",
       "job_id": "67890",
       "timestamp": "2023-11-01T10:00:00Z",
       ...
     }
   }
   ```
