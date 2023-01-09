from functools import reduce

# import json

import pickle


import os.path


from collections import OrderedDict


from hash_util import valid_proof, hash_block


owner = 'Arthur'

MINING_REWARD = 10


GENESIS_BLOCK = {
    'previous_block_hash': '',
    'index': 0,
    'processed_transactions': [],
    'proof': 100
}

blockchain = [GENESIS_BLOCK]


open_transactions = []


participants = {
    'Max'
}


def load_data():
    """Loads the data of the blockchain in a file in your system's storage"""

    # if (not os.path.isfile('blockchain.json')):
    if (not os.path.isfile('blockchain.p')):
        print('No blockchain file detected, loading starting blockchain...')
        return
    # with open('blockchain.json', mode='r') as g: ###versão JSON
    with open('blockchain.p', mode='rb') as g: ####versão PICKLE (rb, read binary) (e também o blockchain.p)
        # read_blockchain, read_transactions = g.readlines() ###VERSÃO JSON
        # global blockchain ###VERSÃO JSON
        # global open_transactions ###VERSÃO JSON
        # blockchain = json.loads(read_blockchain) ##versão JSON

        file_content = pickle.loads(g.read()) # vai ler O CONTEÚDO INTEIRO DE NOSSO ARQUIVO pickle/pickle data no arquivo lido, e aí O METHOD de '.loads()' vai tentar CONVERTER TUDO ISSO EM 'python data' (objects, dicts, tuples, lists, etc)...
        print(file_content, 'LOADED DATA') ## quando recorremos ao pickling/usamos o PICKLE, NÃO TEMOS QUE NOS PREOCUPAR COM A 'PERDA DE INFO SOBRE O FATO DE UM DICT SER ORDERED OU NÃO' ao converter umA DICT EM BINARY DATA( ao contrário da JSON DATA, em que PERDEMOS ESSA INFO AO CONVERTER PYTHON OBJECTS EM JSON STRINGS..) 

        global blockchain
        global open_transactions
        blockchain = file_content['chain']
        open_transactions = file_content['ot']

        # updated_blockchain = []
        # for block in blockchain:
        #     updated_block = {
        #         'previous_block_hash': block['previous_block_hash'],
        #         'index': block['index'],
        #         'proof': block['proof'],
        #         'processed_transactions': [OrderedDict(
        #             [('amount', transaction['amount']), ('recipient', transaction['recipient']), ('sender', transaction['sender'])]) for transaction in block['processed_transactions']]
        #     }
        #     updated_blockchain.append(updated_block)
        # blockchain = updated_blockchain

        # print(json.loads(read_blockchain))

        # open_transactions = [OrderedDict([('amount', transaction['amount']), ('recipient', transaction['recipient']), (
        #     'sender', transaction['sender'])]) for transaction in json.loads(read_transactions)]

        # print(json.loads(read_transactions))


load_data()


def save_data():
    """Saves the data of the blockchain in a file in your system's storage"""

    # with open('blockchain.txt', mode='w') as f: #versão JSON DO CÓDIGO
    #VVVVVV VERSÃO PICKLE do código --> observe o formato de arquivo '.p', que é convencionado para o pickle...
    with open('blockchain.p', mode='wb') as f:   ##versão PICKLE DO CÓDIGO (vai armazenar BINARY DATA no seu arquivo).. --> pq o  default é 'wt' (write text), E O WRITE DE BINARY É 'wb' (write binary)...
        # f.write(json.dumps(blockchain)) #versão JSON do código...
        # f.write('\n')
        # f.write(json.dumps(open_transactions)) 
        # f.write(pickle.dumps(blockchain))   ###versão PICKLE DO CÓDIGO  --> 'pickle.dumps()' CONVERTE NOSSA PYTHON DATA EM _ BINARY DATA DO PICKE, QUE SERÁ ENTÃO ESCRITA NO NOSSO ARQUIVO  por meio de 'f.write()'....
                ####entretanto, se você QUER __ ESCREVER __ BINARY_ _DATA EM 1 ARQUIVO, VOCÊ É OBRIGADO A TROCAR O 'mode' de seu 'open' para o valor de 'wb'...
        ##QUANDO ESTAMOS 'PICKLING', não é POSSÍVEL ADICIONAR LINE BREAKS por meio de '\n', POR ISSO NÃO VAMOS ESCREVER UM 'f.write('\n')' PARA SEPARAR NOSSO CONTEÚDO...
        ## EM VEZ DISSO, VAMOS USAR 1 OBJECT OU DICTIONARY PARA __ SEPARAR _ NOSSOS CONTEÚDOS, PQ ISSO FUNCIONARÁ...
        data_to_save = { #usamos esse dict para SEPARAR NOSSOS CONTEÚDOS (line break) quando o outputtarmos no arquivo de texto...
            'chain': blockchain,
            'ot': open_transactions
        }
        f.write(pickle.dumps(data_to_save))

def get_user_choice():
    """ Returns the input of the user (either 1, 2, h or q) to proceed with the options """
    user_input = input('Please choose an option: ')

    return user_input


def get_transaction_value():
    """ Returns the input of the user (sender, recipient, amount) as a tuple, to proceed with option 1 """

    user_transaction_sender = owner

    user_transaction_recipient = input("Please enter the recipient's name: ")
    if (user_transaction_recipient == '' or not isinstance(user_transaction_sender, str)):
        return None
    user_transaction_amount = input('Please enter transaction amount: ')
    if (user_transaction_amount == '' or not user_transaction_amount.isnumeric() or isinstance(user_transaction_amount, bool)):
        print('TEST')
        return None
    user_transaction_input = (
        user_transaction_sender, user_transaction_recipient, float(user_transaction_amount))
    return user_transaction_input


def add_transaction(sender, recipient, amount=1.0):
    """Faz append de uma NOVA TRANSACTION À LIST DE ' open_transactions, e aí RETORNA TRUE OU FALSE, a depender do sucesso de seu códiogo --> verification para ver se o user pode ou naõ realizar essa operação/send de coins...'....

        Arguments:
    :sender: o sender da transaction (nome ou id)   
    :recipient: o receiver da transaction (nome ou id)
    :amount: a quantidade (DEVE SER UM FLOAT). DEFAULT É 1.0 coin ...            
    """
    new_transaction = OrderedDict([
        ('amount', amount),
        ('recipient', recipient),
        ('sender', sender)
    ])
    if not verify_transaction(new_transaction):
        print('Your funds are not enough for the chosen operation')
        return False
    else:
        open_transactions.append(new_transaction)
        participants.add(sender)
        participants.add(recipient)
        print(open_transactions)
        save_data()
        return True


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def mine_block():
    """É essa função que PROCESSA NOSSAS OPEN TRANSACTIONS, PARA ENTÃO ADICIONAR UM NOVO BLOCK À BLOCKCHAIN """
    previous_block = blockchain[-1]
    hashed_block = hash_block(previous_block)
    proof = 0

    print(hashed_block, 'LINE51251')

    proof = proof_of_work()
    reward_transaction = OrderedDict([
        ('amount', MINING_REWARD),
        ('recipient', owner),
        ('sender', 'ourApp')
    ])
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)

    block = {'previous_block_hash': hashed_block,
             'index': len(blockchain),

             'processed_transactions': copied_transactions,
             'proof': proof
             }
    blockchain.append(block)

    print(blockchain, 'TRIED TO MINE BLOCK')
    return True


def output_blockchain():
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    print(blockchain)
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_block_hash'] != hash_block(blockchain[index - 1]):
            return False

        if not valid_proof(block['processed_transactions'][:-1], block['previous_block_hash'], block['proof']):
            print('Proof of work is invalid.')
            return False
    return True


def verify_transaction(transaction):
    """Retorna True ou False a DEPENDER DO CHECK DA TRANSACTION; SE O USER NÃO TIVER FUNDS SUFICIENTES, RETORNA FALSE E A OPERAÇÃO/TRANSACTION NÃO É REALIZADA. É chamado lá em 'add_transaction()'.."""
    sender_balance = get_balance(transaction['sender'])[2]
    print(sender_balance)
    return sender_balance >= transaction['amount']


def get_value(person):
    return [[transaction['amount'] for transaction in block['processed_transactions'] if transaction[person] == owner] for block in blockchain]


def get_balance(participant):
    transaction_sender = get_value('sender')
    open_transactions_sender = [transaction['amount']
                                for transaction in open_transactions if transaction['sender'] == participant]
    transaction_sender.append(open_transactions_sender)

    print(transaction_sender[0])

    print(transaction_sender)

    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                         if len(tx_amt) > 0 else tx_sum + 0, transaction_sender, 0)

    print(amount_sent)

    transaction_recipient = get_value('recipient')

    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                             if len(tx_amt) > 0 else tx_sum + 0, transaction_recipient, 0)
    print(amount_received)
    return (amount_sent, amount_received, amount_received - amount_sent)


def verify_transactions():

    if open_transactions == []:
        return None
    else:

        return all([verify_transaction(transaction) for transaction in open_transactions])


waiting_for_input = True


while waiting_for_input:

    print('-' * 30)
    print('1: Add a new transaction value')
    print('2: Display current blockchain')
    print('3: Show participants')
    print("b: Show user's balance")
    print('h: Manipulate the chain')
    print('m: Mine a block')
    print('q: Quit the program')
    print('v: Verify open transactions')
    print('-' * 30)
    user_input = get_user_choice()
    if(user_input == '1'):
        user_transaction = get_transaction_value()

        if(user_transaction == None):
            print('Please enter a valid sender, recipient and transaction value.')
        else:
            sender, recipient, amount = user_transaction
            if add_transaction(sender, recipient, amount):
                print('Added transaction!')
            else:
                print('Transaction failed')

    elif(user_input == '2'):
        output_blockchain()
    elif(user_input == 'q'):
        waiting_for_input = False

    elif(user_input == 'h'):
        print(blockchain)
        elementIndex = input(
            'Enter the number of the element you want to manipulate: ')
        if (elementIndex.isnumeric()):
            if (len(blockchain) >= int(elementIndex) + 1):
                elementValue = input(
                    ' Please Enter the value you want to insert: ')
                blockchain[int(elementIndex)]['processed_transactions'] = [
                    {'sender': 'test', 'recipient': 'tested', 'amount': 1212}]
            else:
                print(
                    'No block for that index, please insert sufficient number of blocks before trying to manipulate a specific one')
        else:
            print('Invalid index entered, please try again')

    elif(user_input == 'm'):
        if mine_block():
            print(' MINED')
            open_transactions = []
            save_data()
    elif(user_input == '3'):
        print(participants)
    elif(user_input == 'b'):
        sent, received, balance = get_balance(owner)
        print(f'Blocks sent by {owner}: ' + '{sent:>6.2f}'.format(sent=sent))
        print(f'Blocks received by {owner}: ' +
              '{received:>6.2f}'.format(received=received))
        print(f'Total Balance of {owner}: ' +
              '{balance:>6.2f}'.format(balance=balance))
    elif(user_input == 'v'):
        if (verify_transactions()):
            print('Transactions are valid.')
        elif(verify_transactions() == None):
            print('No transactions to verify, please add a transaction.')
        else:
            print('Invalid transactions detected.')
    else:
        print('-' * 40)
        print('Invalid command, please input 1, 2 or q.')
    if(not verify_chain()):
        print('Blockchain was found invalid.')
        print(blockchain)
        waiting_for_input = False
    else:
        print('Blockchain is valid')


else:
    print('User left')
