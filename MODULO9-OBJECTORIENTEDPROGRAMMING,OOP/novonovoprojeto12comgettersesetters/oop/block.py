
from printable import Printable
from time import time ##vai nos dar o 'currentTime', basicamente....  --> ISSO NOS DÁ O CURRENT TIME, COMO UM NUMBER BEM LONGO...



class Block(Printable): ###inheritamos a class de 'Printable', que COMPARTILHA O REPR DELE a essa class aqui..
    def __init__(self,  previous_block_hash='', index=0, processed_transactions=[], proof=100, timestamp=time() ):
        self.previous_block_hash = previous_block_hash
        self.index = index
        self.processed_transactions = processed_transactions
        self.proof = proof
        self.timestamp = timestamp 
    
    # def __repr__(self):
        # return '{{previous_block_hash: {}, index: {}, processed_transactions: {}, proof: {}, timestamp: {} }}'.format(self.previous_block_hash, self.index, [transaction.__dict__ for transaction in self.processed_transactions], self.proof, self.timestamp) ###eu ia usar esse código, mas o professor queria mostrar a implementação de INHERITANCE, por isso optei pelo código de baixo...

        # return str(self.__dict__)
        # new_print = Printable(self.__dict__)
        
        # return new_print.print() ###exemplo de inheritance
        # return str(self.__dict__)   #mesma coisa que o código de cima, mas MAIS SUCINTO... (mas essa versão não vai converter os object 'transaction' em dicts, por isso a minha versão é melhor  hahahaha)

        # return {'previous_block_hash': self.previous_block_hash,
        #         'index': self.index,
        #         'processed_transactions': self.processed_transactions,
        #         'proof': self.proof,
        #         'timestamp': self.timestamp
        # }