from operator import is_
import string

owner = 'Arthur'


MINING_REWARD = 10 #cota fixa de RETORNO EM COINS PELA TAREFA DE 'MINE_BLOCK'...


GENESIS_BLOCK = {  # será uma CONSTANTE GLOBAL, nunca mudará, por isso o nome em CAPITAL CASE....
    'previous_ block_hash': '',
    'index': 0,
    'processed_transactions': []
}

blockchain = [GENESIS_BLOCK]

participants = {
    'Max'
}

# participants = set() # approach n1 de COMO CRIAR UM SET  (dessa vez, um set vazio)
# participants = set(['Max1', 'Max2']) # approach n2 DE COMO CRIAR UM SET  (dessa vez forrado com valores de nossa iterable/list)...
# participants = {} # approach n3 de COMO CRIAR UM SET, ESSE É O APPROACH MAIS USADO..


open_transactions = []


def get_last_blockchain_value():
    """returns a blockchain"""
    if(len(blockchain) > 0):
        print('blockchain')
        return blockchain[-1]

    return None


def get_user_choice():
    """ Returns the input of the user (either 1, 2, h or q) to proceed with the options """
    user_input = input('Please choose an option: ')

    return user_input


def get_transaction_value():
    """ Returns the input of the user (sender, recipient, amount) as a tuple, to proceed with option 1 """

    user_transaction_sender = owner
    #user_transaction_sender =  input("Please enter the sender's name: ")
    # if (user_transaction_sender == '' or not isinstance(user_transaction_sender, str)):
    #     return None
    user_transaction_recipient = input("Please enter the recipient's name: ")
    if (user_transaction_recipient == '' or not isinstance(user_transaction_sender, str)):
        return None
    user_transaction_amount = input('Please enter transaction amount: ')
    if (user_transaction_amount == '' or not user_transaction_amount.isnumeric() or isinstance(user_transaction_amount, bool)):
        print('TEST')
        return None
    user_transaction_input = (
        user_transaction_sender, user_transaction_recipient, float(user_transaction_amount))
    print(user_transaction_input)
    print(user_transaction_input, 'LINE')
    return user_transaction_input


# def add_value(transaction_amount, last_transaction=[1]):
#     """Faz append de um novo value, assim como o value do ÚLTIMO BLOCKCHAIN, à blockchain global do arquivo

#         Arguments:
#     :transaction_amount: The amount that should be added.
#     :last_transaction: The last blockchain transaction (default [1]).
#     """
#     if (last_transaction == None):
#         return blockchain.append([[1], transaction_amount])

#     blockchain.append([last_transaction, transaction_amount])


def add_transaction(sender, recipient, amount=1.0):
    """Faz append de uma NOVA TRANSACTION À LIST DE ' open_transactions, e aí RETORNA TRUE OU FALSE, a depender do sucesso de seu códiogo --> verification para ver se o user pode ou naõ realizar essa operação/send de coins...'....

        Arguments:
    :sender: o sender da transaction (nome ou id)   
    :recipient: o receiver da transaction (nome ou id)
    :amount: a quantidade (DEVE SER UM FLOAT). DEFAULT É 1.0 coin ...            
    """



    new_transaction = {

        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if not verify_transaction(new_transaction):
        print('Your funds are not enough for the chosen operation')
        return False
    else:
        open_transactions.append(new_transaction)
        participants.add(sender)
        participants.add(recipient)
        print(open_transactions)
        return True


# def mine_block():
#     """É essa função que PROCESSA NOSSAS OPEN TRANSACTIONS, PARA ENTÃO ADICIONAR UM NOVO BLOCK À BLOCKCHAIN """
#     # pass  # pass é usado quando AINDA NÃO QUEREMOS ESCREVER UMA DETERMINADA FUNCTION, QUEREMOS DEIXAR PARA DEPOIS...

#     previous_block = blockchain[-1]
#     # previous_block_values = []
#     hashed_block = ''
#     for key in previous_block:  # nosso loop...
#         value = str(previous_block[key])
#         # previous_block_values.append(value)
#         hashed_block = hashed_block + str(value)
#     # print(previous_block_values)
#     # previous_block_hash = '-'.join(previous_block_values)
#     # print(previous_block_hash, 'LINE')
#     print(hashed_block)
#     block = {'previous_block_hash': hashed_block,

#              'index': len(blockchain),
#              'processed_transactions': open_transactions,
#              # 'previous_block_hash': 'placeholder2',
#              # 'previous_block_hash': previous_block_hash,

#              # 'current_block_hash': 'asasojsaosajoj12o12jojasdopj1', #esse valor será comparado ao VALOR DE 'previous_block_hash' __ DO PRÓXIMO BLOCK, QUANDO O PRÓXIMO BLOCK FOR CRIADO.... (deverão ser equivalentes, esse é o mecanismo de segurança) ---> ATENÇÃO: O HASH DE UM DEWTERMINADO BLOCK É FORMADO A PARTIR DA LISTA DE TRANSACTIONS NO INTERIOR DELE...
#              # totalmente opcional, pq já teremos um index na nossa blockchain; isso so´serve para dizer que 'PODEMOS ADICIONAR METADATA NOS NOSSOS BLOCKS'...

#              }
#     open_transactions.clear()
#     blockchain.append(block)
#     print(blockchain)


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def mine_block():
    """É essa função que PROCESSA NOSSAS OPEN TRANSACTIONS, PARA ENTÃO ADICIONAR UM NOVO BLOCK À BLOCKCHAIN """
    # pass  # pass é usado quando AINDA NÃO QUEREMOS ESCREVER UMA DETERMINADA FUNCTION, QUEREMOS DEIXAR PARA DEPOIS...

    previous_block = blockchain[-1]
    # hashed_block = str([previous_block[key] for key in previous_block]) #feature da LIST COMPREHENSION.... (faz com que evitemos o write de um loop, que e´cumbersome)
    # 'str()' converte essa LISTA DE VALUES em uma string única... que será nosso hash...
    # hashed_block = '-'.join([str(previous_block[key]) for key in previous_block]) #feature da LIST COMPREHENSION.... (faz com que evitemos o write de um loop, que e´cumbersome)
    hashed_block = hash_block(previous_block)
    print(hashed_block)

    reward_transaction = {  #usado para RECOMPENSAR NOSSOS MINERS PELO SEU TRABALHO (pelo add de um novo block à blockchain... esse é o mining)...
        'sender': 'ourApp',
        'recipient': owner,
        'amount': MINING_REWARD


    }

    open_transactions.append(reward_transaction)
    block = {'previous_block_hash': hashed_block,

             'index': len(blockchain),
             'processed_transactions': open_transactions, #nossa 'reward', a REWARD AO 'USER'/instance/miner TAMBÉM SERÁ CONSIDERADA UMA INSTANCE...
             # 'previous_block_hash': 'placeholder2',
             # 'previous_block_hash': previous_block_hash,

             # 'current_block_hash': 'asasojsaosajoj12o12jojasdopj1', #esse valor será comparado ao VALOR DE 'previous_block_hash' __ DO PRÓXIMO BLOCK, QUANDO O PRÓXIMO BLOCK FOR CRIADO.... (deverão ser equivalentes, esse é o mecanismo de segurança) ---> ATENÇÃO: O HASH DE UM DEWTERMINADO BLOCK É FORMADO A PARTIR DA LISTA DE TRANSACTIONS NO INTERIOR DELE...
             # totalmente opcional, pq já teremos um index na nossa blockchain; isso so´serve para dizer que 'PODEMOS ADICIONAR METADATA NOS NOSSOS BLOCKS'...

             }
    # open_transactions.clear()
    blockchain.append(block)
    print(blockchain, 'TRIED TO MINE BLOCK')


def output_blockchain():
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)


# def verify_chain(): #lógica antiga, desatualizada.
#     is_valid = True
#     for block_index in range(len(blockchain)):
#         if block_index == 0:
#             continue
#         elif blockchain[block_index][0] == blockchain[block_index - 1]:
#             print('true')
#             is_valid = True
#         else:
#             is_valid = False
#             break
#         # block_index += 1
#     return is_valid


# def verify_chain(): # minha versão, não é tão CLEAN.
#     '''VERIFY THE CURRENT BLOCKCHAIN AND RETURN TRUE IF VALID, FALSE IF INVALID'''
#     is_valid = True
#     for block_index in range(len(blockchain)):
#         if block_index == 0:
#             continue
#         # elif '-'.join([str(blockchain[block_index - 1][key]) for key in blockchain[block_index - 1]]) == blockchain[block_index ]['previous_block_hash']:
#         elif hash_block(blockchain[block_index - 1]) == blockchain[block_index]['previous_block_hash']:
#             print('true')
#             print(blockchain, 'SUCCESS')
#             is_valid = True
#         else:
#             is_valid = False
#             break
#         # block_index += 1
#     return is_valid


def verify_chain():
    is_valid = True
    # print(blockchain, 'BCHAIN')
    for (index, block) in enumerate(blockchain):
        # print(block['previous_block_hash'] == blockchain[index - 1], 'LINE2151')
        if index == 0:
            continue
        if block['previous_block_hash'] == hash_block(blockchain[index - 1]):
            print('valid block')
        else:
            print('invalid block')
            is_valid = False
    return is_valid

def verify_transaction(transaction):
    """Retorna True ou False a DEPENDER DO CHECK DA TRANSACTION; SE O USER NÃO TIVER FUNDS SUFICIENTES, RETORNA FALSE E A OPERAÇÃO/TRANSACTION NÃO É REALIZADA. É chamado lá em 'add_transaction()'.."""
    sender_balance = get_balance(transaction['sender'])[2]
    return sender_balance >= transaction['amount'] #retornará TRUE OU FALSE....
    # if sender_balance >= transaction['amount']: #mesma coisa que o return da operation logo acima....
    #     return True
    # else:
    #     return False


def get_value(person):
    return [[transaction['amount'] for transaction in block['processed_transactions'] if transaction[person] == owner] for block in blockchain][1]


def get_balance(participant):
    # transaction_sender = [block['processed_transactions'] for block in blockchain
    # transaction_sender = [(transaction for transaction in block['processed_transactions'] if transaction['sender'] == participant) for block in blockchain] ///NÃO FUNCIONA...

    transaction_sent_amount = 0
    transaction_received_amount = 0
    # transaction_sender = [[transaction['amount'] for transaction in block['processed_transactions'] if transaction['sender'] == participant] for block in blockchain][1]
    transaction_sender = get_value('sender')
    open_transactions_sender = [transaction['amount'] for transaction in open_transactions if transaction['sender'] == participant]
    # print(transaction_sender)

    transaction_sender.append(open_transactions_sender) # vai somar os custos/'sent' de todas as TRANSACTIONS JÁ PROCESSADAS + 'open_transactions' que ainda não foram processdas (para que o user não possa adicionar 3 transaction de 10 quando só tem 10 funds, por exemplo...)

    for transaction in transaction_sender:
        print(transaction_sent_amount, transaction[2], 'LINE')
        transaction_sent_amount = transaction_sent_amount + transaction
    # transaction_recipient = [[transaction['amount'] for transaction in block['processed_transactions'] if transaction['recipient'] == participant] for block in blockchain][1]
    transaction_recipient = get_value('recipient')
    for transaction in transaction_recipient:
        transaction_received_amount = transaction_received_amount + transaction

    return (transaction_sent_amount, transaction_received_amount, transaction_received_amount - transaction_sent_amount)


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
    print('-' * 30)
    user_input = get_user_choice()
    if(user_input == '1'):
        user_transaction = get_transaction_value()
        # UNPACKING DE TUPLE.... É EXATAMENTE A MESMA COISA QUE ARRAY DESTRUCTURING.
        
        if(user_transaction == None):
            print('Please enter a valid sender, recipient and transaction value.')
        else:
            sender, recipient, amount = user_transaction
            if add_transaction(sender, recipient, amount):
               print('Added transaction!')
            else:
               print('Transaction failed')


            # add_transaction(user_transaction[0], user_transaction[1], user_transaction[2]) # SINTAXE OLDSCHOOL (sem 'TUPLE UNPACKING', que é basicamente ARRAY DEESTRUCTURING)...
    elif(user_input == '2'):
        output_blockchain()
    elif(user_input == 'q'):
        waiting_for_input = False

    # elif(user_input == 'h'):
    #     elementIndex = input(
    #         'Enter the number of the element you want to manipulate: ')
    #     if (elementIndex.isnumeric()):
    #         if (len(blockchain) >= int(elementIndex) + 1):
    #             elementValue = input(
    #                 ' Please Enter the value you want to insert: ')
    #             blockchain[int(elementIndex)] = [float(elementValue)]
    #         else:
    #             print(
    #                 'No block for that index, please insert sufficient number of blocks before trying to manipulate a specific one')
    #     else:
    #         print('Invalid index entered, please try again')

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
        # se retornou 'True', sucesso, vamos querer que a lista de open_transactions seja LIMPA/resettada...
        if mine_block():
            open_transactions = []
    elif(user_input == '3'):
        print(participants)
    elif(user_input == 'b'):
        sent, received, balance = get_balance(owner)
        print('Blocks sent: ' + str(sent))
        print('Blocks received: ' + str(received))
        print('Total Balance: ' + str(balance))
    else:
        print('-' * 40)
        print('Invalid command, please input 1, 2 or q.')
    if(not verify_chain()):
        # print(blockchain)
        # print(open_transactions)
        # print(verify_chain())
        print('Blockchain was found invalid.')
        print(blockchain)
        waiting_for_input = False
        # break
    else:
        print('Blockchain is valid')
    # print(blockchain, 'LINE')

else:  # complemento do while loop
    print('User left')
