# Simple Blockchain
This project is to help better understand the concept of blockchain


## Components of a Blockchain

### Block

A block is the fundamental component of a block chain. It is made up of 4 main components.

- transaction_data: the raw data that is stored in the block. It can me made of anything, eg. bank transactions, tax records, medical records, game data, software, etc.

- timestamp: when the block was created

- previous_hash: the link to the previous block

- hash: the hash of the current block

- nonce (optional): additional padding that is used for creating a hash. Used in proof of work.

### All Transactions

A list of all transactions

### Chain

A list of all blocks

### Validity

A function to check the validity of the chain

### Proof of Work

A function to perform the proof of work on the block

### Gensis Block

A function to create the incipient block. What makes this unique is that the previous hash is hard coded to 0

### Add new blocks

A function to add blocks to the chain