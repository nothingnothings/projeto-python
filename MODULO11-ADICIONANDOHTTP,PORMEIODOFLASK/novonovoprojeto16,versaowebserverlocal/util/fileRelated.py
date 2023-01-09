
# """HANDLES FILE-SAVING AND FILE-LOADING in our app (saves and loads the blockchain from files)"""


# import json


# from block import Block


# from transaction import Transaction






# __all__ = ['FileAccess']




###class inutilizada, melhor usar esses methods como INSTANCE METHODS em 'blockchain14.py'...

# class FileAccess:







#     @staticmethod
#     def load_data(chain, open_transactions):
#         print(open_transactions)
#         try:
#             with open('blockchain.json', mode='r') as g:
#                 file_content = g.readlines()
#                 chain = json.loads(file_content[0][:-1])
#                 updated_blockchain = []
#                 for block in chain:

#                     converted_tx = [Transaction(
#                         tx['amount'], tx['recipient'], tx['sender']) for tx in block['processed_transactions']]

#                     updated_block = Block(
#                         block['previous_block_hash'], block['index'], converted_tx, block['proof'], block['timestamp'])

#                     updated_blockchain.append(updated_block)
#                 chain = updated_blockchain
#                 open_transactions = json.loads(file_content[1])
#                 print(open_transactions, 'LINE')

#                 updated_transactions = []

#                 for tx in open_transactions:
#                     updated_transaction = Transaction(
#                         tx['amount'], tx['recipient'], tx['sender'])

#                     updated_transactions.append(updated_transaction)
#                 open_transactions = updated_transactions

#         except(IOError, IndexError):
#             print('Handled exception...')

#         finally:
#             print('Your data was or was not loaded. See error statements')
#             print('clean-up work')

#     @staticmethod
#     def save_data(chain, open_transactions):
#         """Saves the data of the blockchain in a file in your system's storage"""
#         try:

#             with open('blockchain.json', mode='w') as f:

#                 converted_transactions = [
#                     tx.__dict__ for tx in open_transactions]

#                 converted_blockchain = [block.__dict__ for block in [Block(block_el.previous_block_hash, block_el.index, [
#                                                                            tx.__dict__ for tx in block_el.processed_transactions], block_el.proof, block_el.timestamp) for block_el in chain]]

#                 for block in converted_blockchain:
#                     for transaction in block['processed_transactions']:
#                         transaction['sender'] = str(transaction['sender'])

#                 for transaction in converted_transactions:
#                     transaction['sender'] = str(transaction['sender'])

#                 f.write(json.dumps(converted_blockchain))
#                 f.write('\n')
#                 f.write(json.dumps(converted_transactions))
#         except IOError:
#             print('Saving failed!')
