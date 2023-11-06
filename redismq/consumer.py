import json
from .base import Base

class Consumer(Base):
    def __init__(self, host, port, db):
        super().__init__(host, port, db)

    def pop(self, key):
        if self.len(key) < 1:
            return None
        return json.loads(self.queue.rpop(key))
