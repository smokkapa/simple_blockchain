from datetime import datetime
from hashlib import sha256

class Block:
    __timestamp         : datetime
    __transaction_data  : any
    __previous_hash     : str
    __hash              : str
    _nonce              : int

    def __init__(self, transaction_data: object, previous_hash: str) -> None:
        self.__timestamp = datetime.now()
        self.__transaction_data = transaction_data
        self.__previous_hash = previous_hash
        self.__hash = self.generate_hash()
        self._nonce = 0

    def __str__(self) -> str:
        return f"""
        Block       : {self.__hash}
        created at  : {self.__timestamp}
        data        : {self.__transaction_data}
        connected to: {self.__previous_hash}
        """
    
    def get_hash(self) -> str:
        return self.__hash

    def get_previous_hash(self) -> str:
        return self.__previous_hash
    
    def get_timestamp(self) -> str:
        return self.__timestamp

    def generate_hash(self) -> str:
        stringified_data = f'{self.__timestamp}{self.__transaction_data}{self.__previous_hash}'
        hash = sha256(stringified_data.encode())
        return hash.hexdigest()
    
