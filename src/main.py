from src.Blockchain.blockchain import Blockchain

all_transaction = [
    {
        'sender'            : 'Bank',
        'recepient'         : 'Shri',
        'transaction_data'  : 'Borrowed $5000.00',
    },
    {
        'sender'            : 'Shri',
        'recepient'         : 'Tesla',
        'transaction_data'  : 'Bought 10 Tsla stocks for $5000.00',
    },
    {
        'sender'            : 'Tesla',
        'recepient'         : 'Shri',
        'transaction_data'  : 'Sold 10 Tsla shares for 10000.00',
    },
    {
        'sender'            : 'Shri',
        'recepient'         : 'Back',
        'transaction_data'  : 'Returned $5500.00 (includes interest)',
    },
]

if __name__ == "__main__":
    my_blockchain = Blockchain()
    for block in all_transaction:
        my_blockchain.add_new_block(block)
    my_blockchain.print_chain()
    print(my_blockchain.proof_of_work(my_blockchain.chain[1]))