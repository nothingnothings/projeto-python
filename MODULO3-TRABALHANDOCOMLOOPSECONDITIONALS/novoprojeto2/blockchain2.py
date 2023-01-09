
# 1o block ---> [[1], 3.5]


# 2o block ---> [[[1], 3.5], 5.8 ]


# 3o block --> [[[[1], 3.5], 5.8], 1.0]



blockchain = []


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


def get_user_transaction_input():
    """ Returns the input of the user (transaction amount) to proceed with option 1 """
    user_transaction_input = input('Please enter your transaction amount: ')
    if (user_transaction_input == '' or not user_transaction_input.isnumeric() or isinstance(user_transaction_input, bool)):
        return None
    else:
        print(user_transaction_input, 'LINE')
        return float(user_transaction_input)


def add_value(transaction_amount, last_transaction=[1]):
    """Faz append de um novo value, assim como o value do ÚLTIMO BLOCKCHAIN, à blockchain global do arquivo

        Arguments:
    :transaction_amount: The amount that should be added.
    :last_transaction: The last blockchain transaction (default [1]).
    """
    if (last_transaction == None):
        return blockchain.append([[1], transaction_amount])

    blockchain.append([last_transaction, transaction_amount])


def output_blockchain():
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20) # O ELSE BLOCK EM FOR/WHILE LOOPS _ SEMPRE __ SERÁ EXECUTADO __ ASSIM QUE __o  LOOP _ TIVER __aCABABADO (acabado de vez)....


# def verify_chain():
#     if(len(blockchain) > 1):
#         for block in blockchain:
#             print(block, 'BLOCK')
#             print(blockchain[blockchain.index(block)][0])
#             if (block != blockchain[blockchain.index(block)][0] or blockchain[blockchain.index(block)][0] != [1]):
#                 print(blockchain[blockchain.index(block)][0])
#                 print('Blockchain appears to be invalid, interrupting execution...')
#                 sys.exit()


# def verify_chain(): #sem o uso da função de 'RANGE()'... --> a range nos dá a info acerca de 'EM QUAL ITERATION DE NOSSO LOOP NÓS ESTAMOS' (iterator),  o que é bem útil...
#     block_index = 0
#     is_valid = True
#     for block in blockchain:
#         if block_index == 0:
#             block_index += 1  # incrementa 1 unidade.
#             continue
#         elif block[0] == blockchain[block_index - 1]:
#             print('true')
#             is_valid = True
#         else:
#             is_valid = False
#             break
#         # sempre teremos de incrementar esse valor, para que nossa comparação ali em cima FUNCIONE....
#         block_index += 1
#     return is_valid


def verify_chain(): #versão alternativa, que usa 'range()'...
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            # block_index += 1  # incrementa 1 unidade. desnecessário quando usamos 'range()'...
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            print('true')
            is_valid = True
        else:
            is_valid = False
            break
        # block_index += 1
    return is_valid











waiting_for_input = True



# while True: ///approach que usava 'breaks' para PARAR NOSSO CÓDIGO _ QUANDO ACONTECIA UM ERRO/APP ERA ENCERRADO....
while waiting_for_input: #approach que usa o SET DE 'global waiting_for_input = False' COMO FORMA DE ENCERRAR A EXECUÇÃO DESSE WHILE LOOP...
    print('-' * 30)
    print('1: Add a new transaction value')
    print('2: Display current blockchain')
    print('h: Manipulate the chain')
    print('q: Quit the program')
    print('-' * 30)
    user_input = get_user_choice()
    if(user_input == '1'):
        tx_amount = get_user_transaction_input()
        if(tx_amount == None):
            print('Please enter a valid value')
        else: 
            add_value(tx_amount, get_last_blockchain_value())
    elif(user_input == '2'):
        output_blockchain()
    elif(user_input == 'q'):
        waiting_for_input = False
        # break
    elif(user_input == 'h'):
        elementIndex = input(
            'Enter the number of the element you want to manipulate: ')
        if (elementIndex.isnumeric()):
            if (len(blockchain) >= int(elementIndex) + 1):
                elementValue = input(' Please Enter the value you want to insert: ')
                blockchain[int(elementIndex)] = [float(elementValue)]
            else:
                print(
                    'No block for that index, please insert sufficient number of blocks before trying to manipulate a specific one')
        else:
            print('Invalid index entered, please try again')
    else:
        print('-' * 40)
        print('Invalid command, please input 1, 2 or q.')
    if(not verify_chain()):
        print(verify_chain())
        print('Blockchain was found invalid.')
        print(blockchain)
        waiting_for_input = False
        # break
    else:
        print('Blockchain is valid')
    print(blockchain)
    # print('Choice registered')

else: #Sim, elses podem ser USADOS TANTO EM WHILE LOOPS COMO EM FOR LOOPS... --> O ELSE CASE SEMPRE É EXECUTADO ___ DEPOIS __ DO FIM DO LOOP (whenever the loop is done)....
    print('User left')