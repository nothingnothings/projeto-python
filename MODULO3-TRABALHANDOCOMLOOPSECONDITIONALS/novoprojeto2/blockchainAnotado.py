

print('STARTED')


blockchain = []


def get_last_blockchain_value():
    """returns a blockchain"""  # exemplo de COMMENT INTERATIVO... (passe o mouse em cima de 'get_last_blockchain_value()' para VER QUE ELE TE DÁ ESSA INFO AÍ...)
    if(len(blockchain) > 0):
        print('blockchain')
        return blockchain[-1]
    # else: /// é opcional, pq podemos só simplesmente colocar aquele outro 'return None' no mesmo level do 'if' para fazer com que ele seja o 'ELSE CASE' sem precisar usar 1 else case (comportamento similar ao do javascript)...
        # return [1] ///PROFESSOR NOS EXPLICA QUE ESSE É UM CÓDIGO PORCO, QUE O RETURN DE '[1]' vai fazer com que o python ASSUMA QUE NOSSOS OUTROS CÓDIGOS POSSUEM UMA LÓGICA ESPECÍFICA, que não é o que ele vai querer... -> por isso ele prefere retornar 'None'...
    return None #approach CLEAN --> será handlado lá em 'add_project', em que esse return é 'CHECKED FOR'...
    # return blockchain[-1]


# def get_user_input():
#     """ Returns the input of the user (a new transaction amount) as a float. """
#     return float(input('Please enter the value of your transaction: '))

def get_user_choice():
    """ Returns the input of the user (either 1 or 2) to proceed with the options """
    # return float(input('Please choose an option: '))
    return input('Please choose an option: ')


def get_user_transaction_input():
    """ Returns the input of the user (transaction amount) to proceed with the option 1 """
    return float(input('Please enter your transaction amount: '))


# essa function usaVA DEFAULT PARAMETERS....
# def add_value(transaction_amount, last_transaction=[1]):
def add_value(transaction_amount, last_transaction=[1]):
    """Faz append de um novo value, assim como o value do ÚLTIMO BLOCKCHAIN, à blockchain global do arquivo

        Arguments:
    :transaction_amount: The amount that should be added.
    :last_transaction: The last blockchain transaction (default [1]).
    """


    if (last_transaction == None):
        blockchain.append([[1], transaction_amount ])
    print(last_transaction)
    blockchain.append([last_transaction, transaction_amount])
    # print(blockchain)

def output_blockchain():
    for block in blockchain:
        print('Outputting block')
        print(block)


# def greet3(name, age=29):  #exemplo de DEFAULT ARGUMENT (argument que é selecionado se o user nao passar parametro algum)...
#     print('Hello ' + name + ', I am ' + age)


# greet3('Arthur') #exemplo de call de function com DEFAULT ARGUMENTS, PQ NÃO CHAMAMOS NADA PARA O SEGUNDO (não passamos a age)....


# print(input_amount)
# # add_value(2, [1])
# add_value(input_amount, [1])

# input_amount = float(input('Please enter the value of your transaction: '))


# add_value(0.9, get_last_blockchain_value())

# input_amount = float(input('Please enter the value of your transaction: '))

# add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.9)  #EXEMPLO DE ___ 'KEYWORD ARGUMENTS' dentro de nossos calls (ou seja, DEIXAMOS DE LADO AQUELA 'IMPORTÂNCIA DA ORDEM' na call de nossas functions...) -> ESSA FUNCTION TERÁ O MESMO EFEITO DAQUELA DE CIMA, MAS COM UMA SINTAXE DIFERENTEZINHA....

# input_amount = float(input('Please enter the value of your transaction: '))


# add_value(transaction_amount=0.9)

# input_amount = float(input('Please enter the value of your transaction: '))


# add_value(0.5, get_last_blockchain_value())

# input_amount = float(input('Please enter the value of your transaction: '))

# add_value(0.34, get_last_blockchain_value())

# print(input_amount)
# add_value(2, [1])
# add_value(get_user_input(), [1])


# add_value(0.9, get_last_blockchain_value())

# # input_amount = float(input('Please enter the value of your transaction: '))


# add_value(last_transaction=get_last_blockchain_value(),
#           transaction_amount=get_user_input())  # EXEMPLO DE ___ 'KEYWORD ARGUMENTS' dentro de nossos calls (ou seja, DEIXAMOS DE LADO AQUELA 'IMPORTÂNCIA DA ORDEM' na call de nossas functions...) -> ESSA FUNCTION TERÁ O MESMO EFEITO DAQUELA DE CIMA, MAS COM UMA SINTAXE DIFERENTEZINHA....

# # input_amount = float(input('Please enter the value of your transaction: '))


# add_value(transaction_amount=get_user_input())

# # input_amount = float(input('Please enter the value of your transaction: '))


# add_value(get_user_input(), get_last_blockchain_value())

# # input_amount = float(input('Please enter the value of your transaction: '))

# add_value(get_user_input(), get_last_blockchain_value())


# while True:
#     # print('THIS IS TRUE')
#     add_value(get_user_input(), get_last_blockchain_value())

#     for block in blockchain:
#         print('Outputting block')
#         print(block)

# while True:
#     print('------------------------------')
#     print('1: Add a new transaction value')
#     print('2: display current blockchain')
#     print('q: Quit the program.')
#     print('------------------------------')
#     user_input = get_user_choice()
#     if(user_input == '1'):
#         tx_amount = get_user_transaction_input()
#         add_value(tx_amount, get_last_blockchain_value())
#     # if(user_input == 2):
#     #     for block in blockchain:
#     #         print('Outputting block')
#     #         print(block)
#     elif(user_input == '2'):
#         output_blockchain()
#     elif(user_input == 'q'):
#         # break
#         continue
#     else:
#         print('----------------------------------------')
#         print('Invalid command, please input 1, 2 or q.')
#     print('Choice registered')

        # for block in blockchain:
        #     print('Outputting block')
        #     print(block)

        # print(blockchain)











while True:
    print('------------------------------')
    print('1: Add a new transaction value')
    print('2: display current blockchain')
    print('q: Quit the program.')
    print('------------------------------')
    user_input = get_user_choice()
    if(user_input == '1'):
        tx_amount = get_user_transaction_input()
        add_value(tx_amount, get_last_blockchain_value())
    # if(user_input == 2):
    #     for block in blockchain:
    #         print('Outputting block')
    #         print(block)
    elif(user_input == '2'):
        output_blockchain()
    elif(user_input == 'q'):
        break
        # continue
    else:
        print('----------------------------------------')
        print('Invalid command, please input 1, 2 or q.')
    print('Choice registered')