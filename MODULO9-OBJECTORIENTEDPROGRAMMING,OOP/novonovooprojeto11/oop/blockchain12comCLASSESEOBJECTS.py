# from functools import reduce

# import json #vamos usar isso para _CONVERTER STRING VALUES em  -LIST VALUES...


# import os.path

# # import hashlib

# # import json

# # isso será/é um ORDERED DICTIONARY (geralmente dictionaries são UNORDERED, mas há use-cases em que ORDER EM DICTIONARIES É ÚTIL, como em casos de 'hashing')...
# from collections import OrderedDict


# from hash_util import valid_proof, hash_block


# OWNER = 'Arthur'

# MINING_REWARD = 10


# # GENESIS_BLOCK = {
# #     'previous_block_hash': '',
# #     'index': 0,
# #     'processed_transactions': [],
# #     'proof': 100
# # }

# # blockchain = [GENESIS_BLOCK]

# blockchain = []


# open_transactions = []

from fileRelated import FileAccess


# participants = {
#     'Max'
# }


# def load_data():
#     global blockchain
#     global open_transactions
#     # """Loads the data of the blockchain in a file in your system's storage"""
#     # with open('blockchain.txt', mode='r') as g:
#     #     if (not os.path.isfile('blockchain.json')):  ##error handling caseiro, que eu escrevi...
#     #         print('No blockchain file detected, loading starting blockchain...')
#     #         return
#     try:
#         with open('blockchain.json', mode='r') as g:
#             read_blockchain, read_transactions = g.readlines()
#             global blockchain
#             global open_transactions
#             blockchain = json.loads(read_blockchain)
#             updated_blockchain = []
#             for block in blockchain:
#                 updated_block = {
#                     'previous_block_hash': block['previous_block_hash'],
#                     'index': block['index'],
#                     'proof': block['proof'],
#                     'processed_transactions': [OrderedDict(
#                         [('amount', transaction['amount']),('recipient', transaction['recipient']),('sender', transaction['sender'])]) for transaction in block['processed_transactions']]
#                 }
#                 updated_blockchain.append(updated_block)
#             blockchain = updated_blockchain
#             # blockchain = json.loads(read_blockchain) #vamos definir nossas  variáveis globais como sendo esse valor....
#             print(json.loads(read_blockchain))
#             # open_transactions = json.loads(read_transactions) #sem list comprehension, e sem UNORDERED DICTS sendo carregados no nosso app (leva a um erro de check/comparação entre PROOF criada a partir de transactions com formato 'ORDERED DICT' e o conteúdo efetivo armazenado nos nossos arquivos, cujo formato das transactions é 'unordered dict')..
#             open_transactions = [OrderedDict([('amount', transaction['amount']),('recipient', transaction['recipient']),('sender', transaction['sender'])]) for transaction  in json.loads(read_transactions)] #com list comprehension...
#             # open_transactions = json.loads(read_transactions)

#             print(json.loads(read_transactions))
#     except IOError: #VAI FAZER CATCH DE QUAISQUER 'INPUT/OUTUPT' errors que ocorrerem nesse block de 'try' (são erros especiais, que devem ser handlados por um except block como esse)...
#     # except (IOError, ValueError):    #podemos elencar mais um 'TYPE' de error a ser 'CATCHED' por esse nosso block... basta escrever dentro desse '()'..
#         print('File not found!') #com isso, será printada essa mensagem em casos desse tipo de error, mas o APP NÃO CRASHARÁ... (handled error, em vez de unhandled)...

#         GENESIS_BLOCK = {   ## ISSO FARÁ COM QUE SEJA POSSÍVEL INICIALIZAR NOSSA BLOCKCHAIN MESMO NO CASE DE 'O ARQUIVO DE SUA BLOCKCHAIN NÃO FOI ENCONTRADO'...
#         'previous_block_hash': '',
#         'index': 0,
#         'processed_transactions': [],
#         'proof': 100
#         }
#         blockchain = [GENESIS_BLOCK]
#         open_transactions = []
#     # except ValueError:
#     #     print('You cannot do that, so you get a Value Error.') #podemos adicionar múltiplos except cases,  MAS NÃO É BOM ADICIONAR EXCEPT CASES DE ERRORS QUE PODEM SER EVITADOS (como esse 'ValueError', value errors de quaisquer naturezas)...
#     # except:
#     #     print('You cannot do that, so you get a generic error. WILDCARD ERROR') # WILDCARD except case, que vai HANDLAR TODOS OS ERRORS QUE NÃO FOREM 'CAUGHT'/handlados nos cases anteriores, mais específicos...
#         #MAS CUIDADO COM ESSE EXCEPT CASE GENÉRICO/WILDCARD, PQ O HANDLE __ DE ERROS EXAGERADO __ TAMBÉM _ NÃO É BOM (handle de 'too many errors' também é ruim)

#     finally:# o FINALLY é um block/statement em try-except __ CUJO __ CÓDIGO SEMPRE É EXECUTADO, TANTO FAZ SE OCORRERAM ERROS/FORAM CATCHEADOS ERRORS OU NÃO...
#         # é por isso que os blocks de 'finally' SÃO BONS DE SEREM USADOS PARA 'clean-up work'..
#         print('Your data was or was not loaded. See error statements')
#         print('clean-up work')


# load_data() # start dessa function AUTOMATICAMENTE, COMO PARTE DO FLOW DE NOSSO CÓDIGO..


# def save_data():
#     """Saves the data of the blockchain in a file in your system's storage"""
#     try:
#         # with open('blockchain.txt', mode='w') as f:
#         with open('blockchain.json', mode='w') as f:
#             # f.write(str(blockchain))  #vai writtar essa LIST como um value de STRING no seu arquivo de texto.... --> mas não queremos fazer isso, pq é suboptimal... melhor armazenar esses valores como __ JSON_ data...
#             f.write(json.dumps(blockchain))
#             f.write('\n') #line break entre linhas de info...
#             f.write(json.dumps(open_transactions))
#     except IOError:
#         print('Saving failed!')


# def get_user_choice():
#     """ Returns the input of the user (either 1, 2, h or q) to proceed with the options """
#     user_input = input('Please choose an option: ')

#     return user_input


# def get_transaction_value():
#     """ Returns the input of the user (sender, recipient, amount) as a tuple, to proceed with option 1 """

#     user_transaction_sender = OWNER

#     user_transaction_recipient = input("Please enter the recipient's name: ")
#     if (user_transaction_recipient == '' or not isinstance(user_transaction_sender, str)):
#         return None
#     user_transaction_amount = input('Please enter transaction amount: ')
#     if (user_transaction_amount == '' or not user_transaction_amount.isnumeric() or isinstance(user_transaction_amount, bool)):
#         print('TEST')
#         return None
#     user_transaction_input = (
#         user_transaction_sender, user_transaction_recipient, float(user_transaction_amount))
#     return user_transaction_input


# def add_transaction(sender, recipient, amount=1.0):
#     """Faz append de uma NOVA TRANSACTION À LIST DE ' open_transactions, e aí RETORNA TRUE OU FALSE, a depender do sucesso de seu códiogo --> verification para ver se o user pode ou naõ realizar essa operação/send de coins...'....

#         Arguments:
#     :sender: o sender da transaction (nome ou id)
#     :recipient: o receiver da transaction (nome ou id)
#     :amount: a quantidade (DEVE SER UM FLOAT). DEFAULT É 1.0 coin ...
#     """
#     new_transaction = OrderedDict([  # sintaxe de CREATE DE DICTIONARIES COM ORDEM/ORDENADOS/ORDERED.... (distintos de DICTIONARIES NORMAIS, QUE NÃO POSSUEM ORDER)...
#         ('amount', amount),
#         ('recipient', recipient),
#         ('sender', sender)
#     ])
#     if not verify_transaction(new_transaction):
#         print('Your funds are not enough for the chosen operation')
#         return False
#     else:
#         open_transactions.append(new_transaction)
#         participants.add(sender)
#         participants.add(recipient)
#         print(open_transactions)
#         save_data()
#         return True


# def proof_of_work():
#     last_block = blockchain[-1]
#     last_hash = hash_block(last_block)
#     proof = 0
#     while not valid_proof(open_transactions, last_hash, proof):
#         proof += 1
#     return proof


# def mine_block():
#     """É essa função que PROCESSA NOSSAS OPEN TRANSACTIONS, PARA ENTÃO ADICIONAR UM NOVO BLOCK À BLOCKCHAIN """
#     previous_block = blockchain[-1]
#     hashed_block = hash_block(previous_block)
#     proof = 0
#     # print(hashed_block)
#     print(hashed_block, 'LINE51251')

#     proof = proof_of_work()
#     reward_transaction = OrderedDict([  # sintaxe de CREATE DE DICTIONARIES COM ORDEM/ORDENADOS/ORDERED.... (distintos de DICTIONARIES NORMAIS, QUE NÃO POSSUEM ORDER)...
#         ('amount', MINING_REWARD),
#         ('recipient', OWNER),
#         ('sender', 'ourApp')
#     ])
#     copied_transactions = open_transactions[:]
#     copied_transactions.append(reward_transaction)


#     block = {'previous_block_hash': hashed_block,
#              'index': len(blockchain),
#              #  'processed_transactions': open_transactions,
#              'processed_transactions': copied_transactions,
#              'proof': proof
#              }
#     blockchain.append(block)
#     # save_data() #código pertinente ---> salva no nosso filesystem, no nosso arquivo 'blockchain.txt', o BLOCKCHAIN E OPEN_tRANSACTIONS ATUAIS..
#     print(blockchain, 'TRIED TO MINE BLOCK')
#     return True


# def output_blockchain():
#     for block in blockchain:
#         print('Outputting block')
#         print(block)
#     else:
#         print('-' * 20)


# def verify_chain():
#     print(blockchain)
#     for (index, block) in enumerate(blockchain):
#         if index == 0:
#             continue
#         if block['previous_block_hash'] != hash_block(blockchain[index - 1]):
#             return False

#         if not valid_proof(block['processed_transactions'][:-1], block['previous_block_hash'], block['proof']):
#             print('Proof of work is invalid.')
#             return False
#     return True


# def verify_transaction(transaction):
#     """Retorna True ou False a DEPENDER DO CHECK DA TRANSACTION; SE O USER NÃO TIVER FUNDS SUFICIENTES, RETORNA FALSE E A OPERAÇÃO/TRANSACTION NÃO É REALIZADA. É chamado lá em 'add_transaction()'.."""
#     sender_balance = get_balance(transaction['sender'])[2]
#     print(sender_balance)
#     return sender_balance >= transaction['amount']


# def get_value(person):
#     return [[transaction['amount'] for transaction in block['processed_transactions'] if transaction[person] == OWNER] for block in blockchain]


# def get_balance(participant):  # versão COM O USO DE REDUCE NA NOSSA LIST...
#     transaction_sender = get_value('sender')
#     open_transactions_sender = [transaction['amount']
#                                 for transaction in open_transactions if transaction['sender'] == participant]
#     transaction_sender.append(open_transactions_sender)

#     print(transaction_sender[0])

#     print(transaction_sender)

#     amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
#                          if len(tx_amt) > 0 else tx_sum + 0, transaction_sender, 0)

#     print(amount_sent)

#     transaction_recipient = get_value('recipient')

#     amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
#                              if len(tx_amt) > 0 else tx_sum + 0, transaction_recipient, 0)
#     print(amount_received)
#     return (amount_sent, amount_received, amount_received - amount_sent)


# def verify_transactions():
#     # return all([True, True, True, False])  --> acaba resolvido para 'False'...
#     if open_transactions == []:
#         return None
#     else:
#         # exemplo de uso de LIST COMPREHENSION COM __ BOOLEAN OPERATORS (verify_transaction(transaction), que é true ou false) __ COM __ ANY()/ALL() (retorna true ou false a partir da existência/inexistência de 'false' nessa list aí)...
#         return all([verify_transaction(transaction) for transaction in open_transactions])


# waiting_for_input = True


# while waiting_for_input:
#     # load_data()
#     print('-' * 30)
#     print('1: Add a new transaction value')
#     print('2: Display current blockchain')
#     print('3: Show participants')
#     print("b: Show user's balance")
#     print('h: Manipulate the chain')
#     print('m: Mine a block')
#     print('q: Quit the program')
#     print('v: Verify open transactions')
#     print('-' * 30)
#     user_input = get_user_choice()
#     if(user_input == '1'):
#         user_transaction = get_transaction_value()

#         if(user_transaction == None):
#             print('Please enter a valid sender, recipient and transaction value.')
#         else:
#             sender, recipient, amount = user_transaction
#             if add_transaction(sender, recipient, amount):
#                 print('Added transaction!')
#             else:
#                 print('Transaction failed')

#     elif(user_input == '2'):
#         output_blockchain()
#     elif(user_input == 'q'):
#         waiting_for_input = False

#     elif(user_input == 'h'):
#         print(blockchain)
#         elementIndex = input(
#             'Enter the number of the element you want to manipulate: ')
#         if (elementIndex.isnumeric()):
#             if (len(blockchain) >= int(elementIndex) + 1):
#                 elementValue = input(
#                     ' Please Enter the value you want to insert: ')
#                 blockchain[int(elementIndex)]['processed_transactions'] = [
#                     {'sender': 'test', 'recipient': 'tested', 'amount': 1212}]
#             else:
#                 print(
#                     'No block for that index, please insert sufficient number of blocks before trying to manipulate a specific one')
#         else:
#             print('Invalid index entered, please try again')

#     elif(user_input == 'm'):
#         if mine_block():
#             print(' MINED')
#             open_transactions = []
#             save_data() #código pertinente ---> salva no nosso filesystem, no nosso arquivo 'blockchain.txt', o BLOCKCHAIN E OPEN_tRANSACTIONS ATUAIS..
#     elif(user_input == '3'):
#         print(participants)
#     elif(user_input == 'b'):
#         sent, received, balance = get_balance(OWNER)
#         print(f'Blocks sent by {OWNER}: ' + '{sent:>6.2f}'.format(sent=sent))
#         print(f'Blocks received by {OWNER}: ' +
#               '{received:>6.2f}'.format(received=received))
#         print(f'Total Balance of {OWNER}: ' +
#               '{balance:>6.2f}'.format(balance=balance))
#     elif(user_input == 'v'):
#         if (verify_transactions()):
#             print('Transactions are valid.')
#         elif(verify_transactions() == None):
#             print('No transactions to verify, please add a transaction.')
#         else:
#             print('Invalid transactions detected.')
#     else:
#         print('-' * 40)
#         print('Invalid command, please input 1, 2 or q.')
#     if(not verify_chain()):
#         print('Blockchain was found invalid.')
#         print(blockchain)
#         waiting_for_input = False
#     else:
#         print('Blockchain is valid')


# else:
#     print('User left')


# from functools import reduce

import json

# import os.path

# from collections import OrderedDict


# from hash_util import valid_proof, hash_block

from functools import reduce

from hash_util import hash_block


from block import Block

from transaction import Transaction


from utility2 import Utility

MINING_REWARD = 10 





# def verify_chain(): ####       outsourceado
#     # print(blockchain)
#     for (index, block) in enumerate(blockchain):
#         if index == 0:
#             continue
#         if block.previous_block_hash != hash_block(blockchain[index - 1]):
#             return False

#         # if not valid_proof(block['processed_transactions'][:-1], block['previous_block_hash'], block['proof']):
#         #     print('Proof of work is invalid.')
#         #     return False
#         if not valid_proof(block.processed_transactions[:-1], block.previous_block_hash, block.proof):
#             print('Proof of work is invalid.')
#             return False
#     return True


# def verify_transaction(transaction): ### outsourceado
#     """Retorna True ou False a DEPENDER DO CHECK DA TRANSACTION; SE O USER NÃO TIVER FUNDS SUFICIENTES, RETORNA FALSE E A OPERAÇÃO/TRANSACTION NÃO É REALIZADA. É chamado lá em 'add_transaction()'.."""
#     # sender_balance = get_balance(transaction['sender'])[2]
#     sender_balance = get_balance(transaction.sender)[2]
#     # print(sender_balance)
#     # return sender_balance >= transaction['amount']
#     return sender_balance >= transaction.amount






##### def get_value(person): ###versão com DICTS
######     return [[transaction['amount'] for transaction in block['processed_transactions'] if transaction[person] == OWNER] for block in blockchain]






# def get_balance(participant):  # versão COM O USO DE REDUCE NA NOSSA LIST...
#     transaction_sender = get_value('sender')
#     open_transactions_sender = [transaction['amount']
###   ###                             for transaction in open_transactions if transaction['sender'] == participant]
#     transaction_sender.append(open_transactions_sender)

#     print(transaction_sender[0])

#     print(transaction_sender)

#     amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
#                          if len(tx_amt) > 0 else tx_sum + 0, transaction_sender, 0)

#     print(amount_sent)

#     transaction_recipient = get_value('recipient')

#     amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
#                              if len(tx_amt) > 0 else tx_sum + 0, transaction_recipient, 0)
#     print(amount_received)
#     return (amount_sent, amount_received, amount_received - amount_sent)









# def verify_transactions(): ####OUTSOURCEADO 
#     # return all([True, True, True, False])  --> acaba resolvido para 'False'...
#     if open_transactions == []:
#         return None
#     else:
#         # exemplo de uso de LIST COMPREHENSION COM __ BOOLEAN OPERATORS (verify_transaction(transaction), que é true ou false) __ COM __ ANY()/ALL() (retorna true ou false a partir da existência/inexistência de 'false' nessa list aí)...
#         return all([verify_transaction(transaction) for transaction in open_transactions])










# def get_user_choice():
#     """ Returns the input of the user (either 1, 2, h or q) to proceed with the options """
#     user_input = input('Please choose an option: ')

#     return user_input






# def get_transaction_value():
#     """ Returns the input of the user (sender, recipient, amount) as a tuple, to proceed with option 1 """

#     user_transaction_sender = OWNER

#     user_transaction_recipient = input("Please enter the recipient's name: ")
#     if (user_transaction_recipient == '' or not isinstance(user_transaction_sender, str)):
#         return None
#     user_transaction_amount = input('Please enter transaction amount: ')
#     if (user_transaction_amount == '' or not user_transaction_amount.isnumeric() or isinstance(user_transaction_amount, bool)):
#         print('TEST')
#         return None
#     user_transaction_input = (
#         user_transaction_sender, user_transaction_recipient, float(user_transaction_amount))
#     return user_transaction_input






# def verify_transaction(transaction):
#     """Retorna True ou False a DEPENDER DO CHECK DA TRANSACTION; SE O USER NÃO TIVER FUNDS SUFICIENTES, RETORNA FALSE E A OPERAÇÃO/TRANSACTION NÃO É REALIZADA. É chamado lá em 'add_transaction()'.."""
#     # sender_balance = get_balance(transaction['sender'])[2]
#     sender_balance = get_balance(transaction.sender)[2]
#     print(sender_balance)
#     # return sender_balance >= transaction['amount']
#     return sender_balance >= transaction.amount






# def output_blockchain():
#     for block in blockchain:
#         print('Outputting block')
#         print(block)
#     # else:
#     #     print('-' * 20)





# waiting_for_input = True ### OUTSOURCEADO PARA 'Node' (a class)...


# while waiting_for_input:
#     # load_data()
#     print('-' * 30)
#     print('1: Add a new transaction value')
#     print('2: Display current blockchain')
#     print('3: Show participants')
#     print("b: Show user's balance")
#     print('h: Manipulate the chain')
#     print('m: Mine a block')
#     print('q: Quit the program')
#     print('v: Verify open transactions')
#     print('-' * 30)
#     user_input = get_user_choice()
#     if(user_input == '1'):
#         user_transaction = get_transaction_value()

#         if(user_transaction == None):
#             print('Please enter a valid sender, recipient and transaction value.')
#         else:
#             sender, recipient, amount = user_transaction
#             if add_transaction(sender, recipient, amount):
#                 print('Added transaction!')
#             else:
#                 print('Transaction failed')

#     elif(user_input == '2'):
#         output_blockchain()
#     elif(user_input == 'q'):
#         waiting_for_input = False

#     elif(user_input == 'h'):
#         print(blockchain)
#         elementIndex = input(
#             'Enter the number of the element you want to manipulate: ')
#         if (elementIndex.isnumeric()):
#             if (len(blockchain) >= int(elementIndex) + 1):
#                 elementValue = input(
#                     ' Please Enter the value you want to insert: ')
#                 blockchain[int(elementIndex)]['processed_transactions'] = [
#                     {'sender': 'test', 'recipient': 'tested', 'amount': 1212}]
#             else:
#                 print(
#                     'No block for that index, please insert sufficient number of blocks before trying to manipulate a specific one')
#         else:
#             print('Invalid index entered, please try again')

#     elif(user_input == 'm'):
#         if mine_block():
#             print(' MINED')
#             open_transactions = []
#             save_data() #código pertinente ---> salva no nosso filesystem, no nosso arquivo 'blockchain.txt', o BLOCKCHAIN E OPEN_tRANSACTIONS ATUAIS..
#     elif(user_input == '3'):
#         print(participants)
#     elif(user_input == 'b'):
#         sent, received, balance = get_balance(OWNER)
#         print(f'Blocks sent by {OWNER}: ' + '{sent:>6.2f}'.format(sent=sent))
#         print(f'Blocks received by {OWNER}: ' +
#               '{received:>6.2f}'.format(received=received))
#         print(f'Total Balance of {OWNER}: ' +
#               '{balance:>6.2f}'.format(balance=balance))
#     elif(user_input == 'v'):
#         # if (verify_transactions()):
#         # if (Utility.verify_transactions(open_transactions, get_balance(OWNER))):
#         new_utility = Utility()
#         if (new_utility.verify_transactions(open_transactions, get_balance(OWNER))):
#             print('Transactions are valid.')
#         # elif(verify_transactions() == None):
#         elif(new_utility.verify_transactions(open_transactions, get_balance(OWNER)) == None):
#             print('No transactions to verify, please add a transaction.')
#         else:
#             print('Invalid transactions detected.') 
#     else:
#         print('-' * 40)
#         print('Invalid command.')
#     # if(not verify_chain()):
#     new_utility = Utility()
#     if(not new_utility.verify_chain(blockchain)):
#         print('Blockchain was found invalid.')
#         print(blockchain)
#         waiting_for_input = False
#     else:
#         print('Blockchain is valid')
# else:
#     print('User left')




# OWNER = 'Arthur'  ##ficará lá na instance de 'Node'...



# blockchain = []


# open_transactions = []






    



# def load_data():
#     global blockchain
#     global open_transactions
#     try:
#         with open('blockchain.json', mode='r') as g:
#             # read_blockchain, read_transactions = g.readlines()
#             file_content = g.readlines()
#             blockchain = json.loads(file_content[0][:-1])
#             updated_blockchain = []
#             for block in blockchain:
#                 # updated_block = {
#                 #     'previous_block_hash': block['previous_block_hash'],
#                 #     'index': block['index'],
#                 #     'proof': block['proof'],
#                     # 'processed_transactions': [OrderedDict(
#                     #     [('amount', transaction['amount']),('recipient', transaction['recipient']),('sender', transaction['sender'])]) for transaction in block['processed_transactions']]
#                 # }
#                 # converted_transaction = [OrderedDict([('amount', transaction['amount']), ('recipient', transaction['recipient']), ('sender', transaction['sender'])]) for transaction in block['processed_transactions']], block['proof']
#                 # updated_block = Block(block['previous_block_hash'], block['index'], converted_transaction, block['timestamp'])



#                 # converted_tx = [OrderedDict([('amount', tx['amount']), ('recipient', tx['recipient']), ('sender', tx['sender'])]) for tx in block['processed_transactions']] ###sem o uso de OBJECTs...

#                 converted_tx = [Transaction(tx['amount'], tx['recipient'], tx['sender']) for tx in block['processed_transactions']]

#                 updated_block = Block(block['previous_block_hash'], block['index'], converted_tx, block['proof'], block['timestamp'])
#                 updated_blockchain.append(updated_block)
#                 blockchain = updated_blockchain
#                 # open_transactions = [OrderedDict([('amount', transaction['amount']), ('recipient', transaction['recipient']), ('sender', transaction['sender'])]) for transaction in json.loads(read_transactions)]  # com list comprehension...
#                 open_transactions = json.loads(file_content[1])
#                 # print(open_transactions)
#             #     updated_transactions = []
    
#             #     for tx in open_transactions:
#             #         updated_transaction = OrderedDict([('amount', tx['amount']), ('recipient', tx['recipient']), ('sender', tx['sender'])])

#             #         updated_transactions.append(updated_transaction)
#             # open_transactions = updated_transactions
#                 updated_transactions = []
    
#                 for tx in open_transactions:
#                     updated_transaction = Transaction(tx['amount'], tx['recipient'], tx['sender'])

#                     updated_transactions.append(updated_transaction)
#             open_transactions = updated_transactions

#     except (IOError, IndexError):
#         print('File not found!')

#         # GENESIS_BLOCK = {
#         # 'previous_block_hash': '',
#         # 'index': 0,
#         # 'processed_transactions': [],
#         # 'proof': 100,
#         # t 'timestamp': 12121212122121
#         # }
#         GENESIS_BLOCK = Block('', 0, [], 100, 0)
#         blockchain = [GENESIS_BLOCK]
#         open_transactions = []

#     # except(ValueError): ###usei isto, mas é meio um workaround... o ideal é não usar esse error type....
#     #     blockchain = [GENESIS_BLOCK]
#     #     open_transactions = []
#     finally:
#         print('Your data was or was not loaded. See error statements')
#         print('clean-up work')












class Blockchain:




    def __init__(self, hosting_node_id):
        GENESIS_BLOCK = Block('', 0, [], 100, 0)
        self.__chain = [GENESIS_BLOCK]    ####PRIVATE ATTRIBUTES, PQ NÃO PODEM SER ACESSADOS DO LADO DE FORA DE SEU OBJECT (pelo menos o IDE vai apitar)...
        self.__open_transactions = []
        self.participants = {'Max'}
        # self.load_data()
        FileAccess.load_data(self.__chain, self.__open_transactions)
        self.hosting_node = str(hosting_node_id)


    

    def get_chain(self):  ###usado para fazer GET de nossa 'private attribute' de chain.. 
        return self.__chain[:]  ##retorna uma CÓPIA DA CHAIN, e não a chain em si (se você manipular essa cópia, nada acontece com a chain de verdade, dentro do nosso object)..



    def get_open_transactions(self):
            return self.__open_transactions[:]

        
    # def load_data(self):
    #     # global blockchain  ##agora essas variables serão INTERNAS a 'Blockchain'..
    #     # global open_transactions
    #     try:
    #         with open('blockchain.json', mode='r') as g:
    #             file_content = g.readlines()
    #             self.chain = json.loads(file_content[0][:-1])
    #             updated_blockchain = []
    #             for block in self.chain:
    #                 # converted_tx = [Transaction(tx['amount'], tx['recipient'], tx['sender']) for tx in block.processed_transactions]
    #                 converted_tx = [Transaction(tx['amount'], tx['recipient'], tx['sender']) for tx in block['processed_transactions']]
    #                 # converted_tx = [Transaction(tx['amount'], tx['recipient'], tx['sender']) for tx in block['processed_transactions']]
    #                 updated_block = Block(block['previous_block_hash'], block['index'], converted_tx, block['proof'], block['timestamp'])
    #                 # updated_block = Block(block.previous_block_hash, block.index, converted_tx, block.proof, block.timestamp)
    #                 updated_blockchain.append(updated_block)
    #             self.chain = updated_blockchain
    #             self.open_transactions = json.loads(file_content[1])

    #             updated_transactions = []
        
    #             for tx in self.open_transactions:
    #                 updated_transaction = Transaction(tx['amount'], tx['recipient'], tx['sender'])

    #                 updated_transactions.append(updated_transaction)
    #             self.open_transactions = updated_transactions

    #     except(IOError, IndexError):
    #         print('Handled exception...')
    #         # GENESIS_BLOCK = Block('', 0, [], 100, 0)  
    #         # self.chain = [GENESIS_BLOCK]  ##código desnecessário, pq agora será TRANSPLANTADO LÁ PARA o '__init__()' (vamos INICIALIZAR NOSSA BLOCKCHAIN LÁ... SE UMA BLOCKCHAIN NÃO EXISTIR, ESSA LÓGICA ALI DE BAIXO _ VAI __o CRIAR, com '[genesis_block]' no seu interior... -> esse value de '[genesis_block]' vai ser OVERWRITTADO quando forem minerados mais blocks, por meio da function de 'load_data'...)
    #         # self.open_transactions = []
    #     finally:
    #         print('Your data was or was not loaded. See error statements')
    #         print('clean-up work')

# load_data() ###agora será chamado de DENTRO DO CONSTRUCTOR DE 'Blockchain'....

    def proof_of_work(self):
    # last_block = blockchain[-1]
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        # while not valid_proof(open_transactions, last_hash, proof):
        # new_utility = Utility() ####versão bosta do código de 'helper class' (pq vamos querer que essa class tenha METHODS ESTÁTICOS, e não METHODS/ATTRIBUTOS DE 'INSTANCE')...
        # while not Utility.valid_proof(open_transactions, last_hash, proof):
        # while not new_utility.valid_proof(open_transactions, last_hash, proof):
        while not Utility.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof




    def get_value(self, person):  # versão com OBJECTS (block) NO LUGAR DE 'dicts'...
        # return [[transaction.amount for transaction in block.processed_transactions if getattr(transaction, person) == OWNER] for block in blockchain]
        return [[transaction.amount for transaction in block.processed_transactions if getattr(transaction, person) == self.hosting_node] for block in self.__chain]


    def get_balance(self, participant):  # versão COM O USO DE REDUCE NA NOSSA LIST...
        transaction_sender = self.get_value('sender')
        open_transactions_sender = [transaction.amount
                                    for transaction in self.open_transactions if transaction.sender == participant]
                                    
        transaction_sender.append(open_transactions_sender)

        print(transaction_sender[0])

        print(transaction_sender)

        amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                            if len(tx_amt) > 0 else tx_sum + 0, transaction_sender, 0)

        print(amount_sent)

        transaction_recipient = self.get_value('recipient')

        amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                                if len(tx_amt) > 0 else tx_sum + 0, transaction_recipient, 0)
        print(amount_received)
        return (amount_sent, amount_received, amount_received - amount_sent)


    # def save_data(self): ## para o save de nossa data, nesse caso concreto, a 'ORDER DE NOSSAS DICTS' não interessa, pq só vamos ARMAZENAR AS TRANSACTIONS EM UM ARQUIVO JSON, e não 'checar a validade' de nossa blockchain/transactions (isso é apenas feito lá nos methods de VERIFY, em 'hash_util.py')...
    #     """Saves the data of the blockchain in a file in your system's storage"""
    #     try:
    #         # with open('blockchain.txt', mode='w') as f:
    #         with open('blockchain.json', mode='w') as f:
    #             # f.write(str(blockchain))  #vai writtar essa LIST como um value de STRING no seu arquivo de texto.... --> mas não queremos fazer isso, pq é suboptimal... melhor armazenar esses valores como __ JSON_ data...
    #             # print(open_transactions)
    #             # print(open_transactions)
    #             # converted_transactions = []

    #             # for transaction in open_transactions:
    #             #     converted_transactions.append(Transaction(transaction['amount'], transaction['recipient'], transaction['sender']))
    #             # converted_transactions = [transaction.__dict__ for transaction in converted_transactions]
    #             ##mesma coisa que isto:
    #             # converted_transactions = [Transaction(transaction['amount'], transaction['recipient'], transaction['sender']).__dict__ for transaction  in open_transactions]

    #             # converted_transactions = [tx.__dict__ for tx in open_transactions]
    #             converted_transactions = [tx.__dict__ for tx in self.open_transactions]


    #             # converted_blockchain = [] ### meu código, que não funcionou...
    #             # for block in blockchain:
    #             #     # não é necessário '.__dict__.copy()' aqui pQ NÃO VAMOS MANIPULAR ESSE DICT (situação diferente daquela vista em 'hash_block', pq lá VAMOS MANIPULAR NOSSO DICT)....
    #             #     converted_blockchain.append(block.__dict__) ###vai converter todos nossos 'block' (formato OBJECT 'BLOCK') em DICTS, dicts que então poderemos usar naquele CONVERSOR JSON (pq as DICTS são compatíveis com a conversão para json, ao passo que 'objects', não)...
                

                
    #             # for block in converted_blockchain:
    #             #     dict_transactions = []
    #             #     for transaction in block['processed_transactions']:
    #             #         # dict_transactions.append(transaction.to_ordered_dict())
    #             #         dict_transactions.append(transaction.__dict__)
    #             #     block['processed_transactions'] = dict_transactions

    #             #código do professor...  --> o objetivo desse código era CONVERTER AO MESMO TEMPO OS BLOCKS E AS TRANSACTIONS (dentro de cada um desses block objects) EM DICTS...
    #             # converted_blockchain = [block.__dict__ for block in [ Block(block_el.previous_block_hash, block_el.index, [tx.__dict__ for tx in block_el.processed_transactions], block_el.proof, block_el.timestamp) for block_el in blockchain ]  ] ##'block_el' é originalmente um OBJECT.... por isso a refeerncia a seus valores, nessa list comprehension,... --> queremos converter TANTO OS OBJECTS 'Block' como 'Transacion' EM __ DICTS__, PARA QUE POSSAM SER ARMAZENADOS COMO JSON DATA EM ARQUVIOS JSON/TEXT...
    #             converted_blockchain = [block.__dict__ for block in [ Block(block_el.previous_block_hash, block_el.index, [tx.__dict__ for tx in block_el.processed_transactions], block_el.proof, block_el.timestamp) for block_el in self.chain]  ] ##'block_el' é originalmente um OBJECT.... por isso a refeerncia a seus valores, nessa list comprehension,... --> queremos converter TANTO OS OBJECTS 'Block' como 'Transacion' EM __ DICTS__, PARA QUE POSSAM SER ARMAZENADOS COMO JSON DATA EM ARQUVIOS JSON/TEXT...
                

    #             for block in converted_blockchain:
    #                 for transaction in block['processed_transactions']:
    #                     transaction['sender'] = str(transaction['sender'])

    #             for transaction in converted_transactions:
    #                 transaction['sender'] = str(transaction['sender'])


    #             f.write(json.dumps(converted_blockchain))
    #             f.write('\n') #line break entre linhas de info...
    #             f.write(json.dumps(converted_transactions))
    #     except IOError: 
    #         print('Saving failed!')


    def mine_block(self):
        """É essa função que PROCESSA NOSSAS OPEN TRANSACTIONS, PARA ENTÃO ADICIONAR UM NOVO BLOCK À BLOCKCHAIN """

        # previous_block = blockchain[-1]
        previous_block = self.__chain[-1]
        print(previous_block)
        # print(blockchain[-1])
        hashed_block = hash_block(previous_block)
        print(hashed_block)
        print(hashed_block)
        # proof = 0

        # proof = proof_of_work()
        proof = self.proof_of_work()
        # reward_transaction = OrderedDict([  # sintaxe de CREATE DE DICTIONARIES COM ORDEM/ORDENADOS/ORDERED.... (distintos de DICTIONARIES NORMAIS, QUE NÃO POSSUEM ORDER)...
        #     ('amount', MINING_REWARD),
        #     ('recipient', OWNER),
        #     ('sender', 'ourApp')
        # ])
        reward_transaction = Transaction(MINING_REWARD, self.hosting_node, 'ourApp')
        # copied_transactions = open_transactions[:]
        copied_transactions = self.__open_transactions[:]
        copied_transactions.append(reward_transaction)


        # block = Block(hashed_block, len(blockchain), copied_transactions, proof)
        block = Block(hashed_block, len(self.__chain), copied_transactions, proof)
        # blockchain.append(block)
        self.__chain.append(block)
        self.open_transactions = []
        # self.save_data()
        FileAccess.save_data(self.__chain, self.__open_transactions)
        # save_data() #código pertinente ---> salva no nosso filesystem, no nosso arquivo 'blockchain.txt', o BLOCKCHAIN E OPEN_tRANSACTIONS ATUAIS..
        print(self.__chain, 'TRIED TO MINE BLOCK')
        return True












    def add_transaction(self, sender, recipient, amount=1.0):
        """Faz append de uma NOVA TRANSACTION À LIST DE ' open_transactions, e aí RETORNA TRUE OU FALSE, a depender do sucesso de seu códiogo --> verification para ver se o user pode ou naõ realizar essa operação/send de coins...'....

            Arguments:
        :sender: o sender da transaction (nome ou id)   
        :recipient: o receiver da transaction (nome ou id)
        :amount: a quantidade (DEVE SER UM FLOAT). DEFAULT É 1.0 coin ...            
        """
        # new_transaction = OrderedDict([  # sintaxe de CREATE DE DICTIONARIES COM ORDEM/ORDENADOS/ORDERED.... (distintos de DICTIONARIES NORMAIS, QUE NÃO POSSUEM ORDER)...
        #     ('amount', amount),
        #     ('recipient', recipient),
        #     ('sender', sender)
        # ])


        new_transaction = Transaction(amount, recipient, sender)
        # if not verify_transaction(new_transaction)

        # if not Utility.verify_transaction(new_transaction, get_balance(OWNER)):
        if not Utility.verify_transaction(new_transaction, self.get_balance):
            print('Your funds are not enough for the chosen operation')
            return False
        else:
            self.open_transactions.append(new_transaction)
            self.participants.add(sender)
            self.participants.add(recipient)
            print(self.open_transactions)
            # self.save_data()
            FileAccess.save_data(self.__chain, self.__open_transactions)
            return True
