
owner = 'Arthur'

MINING_REWARD = 10



GENESIS_BLOCK = {
    'previous_ block_hash': '',
    'index': 0,
    'processed_transactions': []
}

blockchain = [GENESIS_BLOCK]


open_transactions = []


participants = {
    'Max'
}


# def get_last_blockchain_value():
#     """returns a blockchain"""
#     if(len(blockchain) > 0):
#         print('blockchain')
#         return blockchain[-1]
#     return None


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


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def mine_block():
    """É essa função que PROCESSA NOSSAS OPEN TRANSACTIONS, PARA ENTÃO ADICIONAR UM NOVO BLOCK À BLOCKCHAIN """
    previous_block = blockchain[-1]
    hashed_block = hash_block(previous_block)
    print(hashed_block)

    reward_transaction = {
        'sender': 'ourApp',
        'recipient': owner,
        'amount': MINING_REWARD

    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {'previous_block_hash': hashed_block,
             'index': len(blockchain),
            #  'processed_transactions': open_transactions,
            'processed_transactions': copied_transactions
             }
    blockchain.append(block)
    print(blockchain, 'TRIED TO MINE BLOCK')


def output_blockchain():
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    is_valid = True

    for (index, block) in enumerate(blockchain):

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
    print(sender_balance)
    return sender_balance >= transaction['amount']


def get_value(person):
        return [[transaction['amount'] for transaction in block['processed_transactions'] if transaction[person] == owner] for block in blockchain]


def get_balance(participant):
    transaction_sender = get_value('sender')
    open_transactions_sender = [transaction['amount'] for transaction in open_transactions if transaction['sender'] == participant]
    transaction_sender.append(open_transactions_sender)

    amount_sent = 0
    for tx in transaction_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    transaction_recipient = get_value('recipient')
    amount_received = 0
    for tx in transaction_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return (amount_sent, amount_received, amount_received - amount_sent)





# def verify_transactions(): #versão sem ser 1 LINHA SÓ...
#     transactions_to_verify = []
#     for transaction in open_transactions:
#         transaction_is_valid = verify_transaction(transaction)
#         transactions_to_verify.append(transaction_is_valid)
#     # print(transactions_to_verify)
#     if transactions_to_verify == []:
#         return None
#     return all(transactions_to_verify)



def verify_transactions():
    #return all([True, True, True, False])  --> acaba resolvido para 'False'...
    if open_transactions == []:
        return None
    else:
        return all([verify_transaction(transaction) for transaction in open_transactions]) #exemplo de uso de LIST COMPREHENSION COM __ BOOLEAN OPERATORS (verify_transaction(transaction), que é true ou false) __ COM __ ANY()/ALL() (retorna true ou false a partir da existência/inexistência de 'false' nessa list aí)...







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
            open_transactions = []
    elif(user_input == '3'):
        print(participants)
    elif(user_input == 'b'):
        sent, received, balance = get_balance(owner)
        print('Blocks sent: ' + str(sent))
        print('Blocks received: ' + str(received))
        print('Total Balance: ' + str(balance))
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
