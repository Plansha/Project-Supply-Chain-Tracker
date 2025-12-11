import hashlib
import time
import json

class Block:
    def __init__(self, index, step, prev_hash, timestamp=None):
        self.index = index
        self.step = step
        self.prev_hash = prev_hash
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Create SHA256 hash of block data"""
        block_string = json.dumps({
            "index": self.index,
            "step": self.step,
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
