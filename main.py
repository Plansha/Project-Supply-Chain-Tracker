from blockchain import SupplyChainBlockchain

def run_demo():
    print("SUPPLY CHAIN TRACKER DEMO STARTING...")

    # Create blockchain
    blockchain = SupplyChainBlockchain()

    # Add normal supply chain steps
    print("\n STEP 1: Adding normal supply chain...")
    blockchain.add_step("Manufactured at Factory")
    blockchain.add_step("Packed for Shipping")
    blockchain.add_step("Shipped to Warehouse")
    blockchain.add_step("Delivered to Retailer")

    # Show valid chain
    blockchain.print_chain()
    print(f"\n Chain Valid? {blockchain.is_chain_valid()}")

    # TAMPER ATTACK!
    print("\n STEP 2: SIMULATING TAMPER ATTACK...")
    blockchain.chain[2].step = "LOST IN TRANSIT!"  # Change block #2
    print(f"\nChanged Block #2 step to: '{blockchain.chain[2].step}'")

    # Show broken chain
    blockchain.print_chain()
    print(f"\n Chain Valid? {blockchain.is_chain_valid()}")

    print("\n DEMO COMPLETE! Tampering detected!")

if __name__ == "__main__":
    run_demo()
