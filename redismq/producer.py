import redis
import json
from typing import Dict
from .base import Base


class Producer(Base):
    def __init__(self, host, port, db):
        super().__init__(host, port, db)

    def push(self, key, value: Dict or str):
        if isinstance(value, str):
            return self.queue.lpush(key, value)
        return self.queue.lpush(key, json.dumps(value))
