# Project-Supply-Chain-Tracker
Supply Chain Tracker – Blockchain Demo
Simple educational blockchain demonstrating tamper-proof supply chain tracking.
Tracks product journey from factory to retailer using cryptographic hashing.
Pure Python 3 implementation – no external libraries needed – runs anywhere.

Features
Immutable block structure using SHA256 hashing
Automatic chain validation to detect tampering
Live demo shows normal supply chain flow plus a simulated attack
Human-readable, pretty-printed blockchain output in the terminal

How It Works
Creates a genesis block representing “Factory Ready”.
Each new supply chain step (manufactured, packed, shipped, delivered, etc.) is stored as a new block.
Every block stores the hash of the previous block, forming a secure hash chain.
If any block’s data is modified, its hash no longer matches and the chain validation fails, exposing tampering.
The included demo script:
Builds a valid chain with several supply chain steps.
Prints the full chain and shows that validation passes.
Then manually tampers with one block’s data and reruns validation, which fails to prove the chain is no longer trustworthy.

Project Structure
block.py – Defines the Block class and hash calculation logic.
blockchain.py – Implements SupplyChainBlockchain for managing the chain, validation, and printing.
main.py – Demo runner that builds the chain, simulates tampering, and prints results.

Requirements
Python 3.x
No third-party libraries required (only hashlib, time, and json from the standard library).

Usage
Clone or download this repository, then run:
bash
python main.py

You should see:
A valid supply chain built step by step.
The blockchain printed with block index, step description, timestamps, and truncated hashes.
Chain validity reported as True before tampering and False after tampering.

Educational Goals
This project is designed for:
Understanding core blockchain concepts: blocks, hashes, previous-hash linkage, and immutability.
Demonstrating how even a tiny change in historical data breaks trust in the whole chain.

