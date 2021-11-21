from src.Block.block import Block

class Blockchain:
    chain              : list[int]
    all_transactions   : list[object]
    
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.__genesis_block()

    def __genesis_block(self) -> None:
        genesis_block = Block('', 0)
        self.chain.append(genesis_block)

    def add_new_block(self, transaction_data) -> None:
        new_block = Block(transaction_data, self.chain[-1].generate_hash())
        self.all_transactions.append(transaction_data)
        self.chain.append(new_block)
    
    def validate_chain(self) -> str:
        valid: bool = True
        for block_index in range(1, len(self.chain)):
            current_block = self.chain[block_index]
            previous_block = self.chain[block_index-1]

            if current_block.generate_hash() != current_block.get_hash():
                valid = False
            if previous_block.generate_hash() != current_block.get_previous_hash():
                valid = False
            
            if not valid:
                break
        
        return 'Blockchain is valid' if valid else 'Blockchain is not valid'
    
    def proof_of_work(self, block: Block, difficulty: int = 10) -> str:
        proof = block.generate_hash()
        while True:
            if proof[:difficulty] == '0'*difficulty:
               break
            block._nonce += 1
            proof = block.generate_hash()
        block._nonce = 0
        return proof


    def print_chain(self) -> None:
        for block in self.chain:
            print(block)
            
