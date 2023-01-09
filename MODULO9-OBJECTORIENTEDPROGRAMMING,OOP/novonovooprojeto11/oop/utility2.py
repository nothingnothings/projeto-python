

# class Util:  ### código que NÃO FUNCIONOu....
#     def __init__(self):
#         print('something')

#     @staticmethod
#     # def valid_proof(self, transactions, previous_block_hash, proof):
#     def valid_proof(transactions, previous_block_hash, proof):

#         ordered_transactions = [transaction.to_ordered_dict()
#                                 for transaction in transactions]

#         verifiable_transactions = json.dumps(ordered_transactions)

#         guess = (str(verifiable_transactions) +
#                  str(previous_block_hash) + str(proof)).encode()

#         guess_hash = hash_string_256(guess)

#         return guess_hash[0:4] == '0000'

#     # @staticmethod
#     @classmethod
#     def verify_chain(cls, blockchain):
#         for (index, block) in enumerate(blockchain):
#             if index == 0:
#                 continue
#             if block.previous_block_hash != hash_block(blockchain[index - 1]):
#                 return False

#             if not cls.valid_proof(block.processed_transactions[:-1], block.previous_block_hash, block.proof):
#                 print('Proof of work is invalid.')
#                 return False
#         return True

# #   @staticmethod
#     @classmethod
#     def get_balance(cls, participant, open_transactions, blockchain):
#         transaction_sender = cls.get_value('sender', blockchain, participant)
#         open_transactions_sender = [transaction.amount
#                                     for transaction in open_transactions if transaction.sender == participant]

#         transaction_sender.append(open_transactions_sender)

#         print(transaction_sender[0])

#         print(transaction_sender)

#         amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
#                             if len(tx_amt) > 0 else tx_sum + 0, transaction_sender, 0)

#         print(amount_sent)

#         transaction_recipient = cls.get_value('recipient', blockchain, participant)

#         amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
#                                 if len(tx_amt) > 0 else tx_sum + 0, transaction_recipient, 0)
#         print(amount_received)
#         return (amount_sent, amount_received, amount_received - amount_sent)

#     @staticmethod
#     def get_value(person, blockchain, owner):  # versão com OBJECTS (block) NO LUGAR DE 'dicts'...
#         return [[transaction.amount for transaction in block.processed_transactions if getattr(transaction, person) == owner] for block in blockchain]

#     # @staticmethod
#     @classmethod
#     def verify_transaction(cls, transaction, open_transactions, blockchain):
#         """Retorna True ou False a DEPENDER DO CHECK DA TRANSACTION; SE O USER NÃO TIVER FUNDS SUFICIENTES, RETORNA FALSE E A OPERAÇÃO/TRANSACTION NÃO É REALIZADA. É chamado lá em 'add_transaction()'.."""
#         # sender_balance = get_balance(transaction.sender)[2]
#         sender_balance = cls.get_balance(transaction.sender, open_transactions, blockchain)[2]
#         return sender_balance >= transaction.amount

#     # @staticmethod
#     @classmethod
#     def verify_transactions(cls, open_transactions):

#         if open_transactions == []:
#             return None
#         else:
#             # exemplo de uso de LIST COMPREHENSION COM __ BOOLEAN OPERATORS (verify_transaction(transaction), que é true ou false) __ COM __ ANY()/ALL() (retorna true ou false a partir da existência/inexistência de 'false' nessa list aí)...
#             return all([cls.verify_transaction(transaction) for transaction in open_transactions])




import json

from hash_util import hash_string_256, hash_block

# from functools import reduce





###versão normal (sem STATIC METHODS)

# class Utility:
#     def verify_chain(self, blockchain):
#         for(index, block) in enumerate(blockchain.chain):
#             if index == 0:
#                 continue
#             if block.previous_block_hash != hash_block(blockchain.chain[index - 1]):
#                 return False

#             if not self.valid_proof(block.processed_transactions[:-1], block.previous_block_hash, block.proof):
#                 print('Proof of work is invalid.')
#                 return False
#         return True

#     def verify_transaction(self, transaction, get_balance):

#         sender_balance = get_balance(transaction.sender)[2]
#         return sender_balance >= transaction.amount

#     def verify_transactions(self, open_transactions, get_balance):
#         return all([self.verify_transaction(transaction, get_balance) for transaction in open_transactions])


#     def valid_proof(self, transactions, previous_block_hash, proof):

#         ordered_transactions = [transaction.to_ordered_dict()
#                                 for transaction in transactions]

#         verifiable_transactions = json.dumps(ordered_transactions)

#         guess = (str(verifiable_transactions) +
#                  str(previous_block_hash) + str(proof)).encode()

#         guess_hash = hash_string_256(guess)
#         print(guess_hash)

#         return guess_hash[0:5] == '00000'










##versão com STATIC METHODS (melhor, pq usamos isso para utility functions):





class Utility:

    @staticmethod
    def verify_chain(blockchain, valid_proof):
        # for(index, block) in enumerate(blockchain.chain):
        for(index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_block_hash != hash_block(blockchain[index - 1]):
                return False

            if not valid_proof(block.processed_transactions[:-1], block.previous_block_hash, block.proof):
                print('Proof of work is invalid.')
                return False
        return True




    # @classmethod  ###FUNCIONA QUASE DE MANEIRA IDÊNTICA AO CÓDIGO VISTO LOGO ACIMA, MAS _ POR SER UM CLASS METHOD, ACABA ACESSANDO METHODS (como 'valid_proof') DENTRO DESSA NOSSA CLASS AQUI..
    # def verify_chain(cls, blockchain):
    #     for(index, block) in enumerate(blockchain.chain):
    #         if index == 0:
    #             continue
    #         if block.previous_block_hash != hash_block(blockchain.chain[index - 1]):
    #             return False

    #         if not cls.valid_proof(block.processed_transactions[:-1], block.previous_block_hash, block.proof):
    #             print('Proof of work is invalid.')
    #             return False
    #     return True



    @staticmethod
    def verify_transaction(transaction, get_balance):

        sender_balance = get_balance(transaction.sender)[2]
        return sender_balance >= transaction.amount


    @staticmethod                                             ###precisa ser chamado lá na function, provavelmente com 'Utility.verify_transaction' (passamos só o POINTER a essa function...).
    def verify_transactions(open_transactions, get_balance, verify_transaction):
        return all([verify_transaction(transaction, get_balance) for transaction in open_transactions])





    @staticmethod
    def valid_proof(transactions, previous_block_hash, proof):

        ordered_transactions = [transaction.to_ordered_dict()
                                for transaction in transactions]

        verifiable_transactions = json.dumps(ordered_transactions)

        guess = (str(verifiable_transactions) +
                 str(previous_block_hash) + str(proof)).encode()

        guess_hash = hash_string_256(guess)
        print(guess_hash)

        return guess_hash[0:5] == '00000'


