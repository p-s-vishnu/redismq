import redis
import json
from typing import Dict

class Base:
    def __init__(self, host="localhost", port=6379, db=0):
        self.queue = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
            retry_on_timeout=True,
        )

    def len(self, key):
        return self.queue.llen(key)