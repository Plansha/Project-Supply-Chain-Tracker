import time
from block import Block

class SupplyChainBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """First block in chain"""
        return Block(0, "Genesis - Factory Ready", "0")

    def add_step(self, step):
        """Add new supply chain step"""
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), step, prev_block.hash)
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        """Check if chain is tamper-proof"""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calculate_hash():
                return False

            if current.prev_hash != previous.hash:
                return False
        return True

    def print_chain(self):
        """Pretty print entire chain"""
        print("\n" + "="*60)
        print("SUPPLY CHAIN TRACKER - BLOCKCHAIN")
        print("="*60)
        for block in self.chain:
            print(f"Block #{block.index}")
            print(f"  Step: {block.step}")
            print(f"  Time: {time.ctime(block.timestamp)}")
            print(f"  Hash: {block.hash[:16]}...")
            print(f"  Prev: {block.prev_hash[:16]}...")
            print("-" * 40)
