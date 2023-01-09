
from util.printable import Printable
from time import time






__all___ = ['Block']

class Block(Printable):
    def __init__(self,  previous_block_hash='', index=0, processed_transactions=[], proof=100, timestamp=time()):
        self.previous_block_hash = previous_block_hash
        self.index = index
        self.processed_transactions = processed_transactions
        self.proof = proof
        self.timestamp = timestamp