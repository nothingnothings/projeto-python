

print('STARTED')


# blockchain = [[1]]

blockchain = []

# def add_value(transaction):
#     blockchain.append(5.3)
#     print(transaction)
#     print(blockchain)


# def add_value(transaction):
#     blockchain.append([blockchain[blockchain. - 1] + transaction]) este código NÃO FUNCIONA.


# essa function faz EXATAMENTE 1 ÚNICA COISA, o que é ótimo....
def get_last_blockchain_value():
    """returns a blockchain""" #exemplo de COMMENT INTERATIVO... (passe o mouse em cima de 'get_last_blockchain_value()' para VER QUE ELE TE DÁ ESSA INFO AÍ...)
    return blockchain[-1]








# input_amount = float(input('Please enter the value of your transaction: '))




def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input('Please enter the value of your transaction: '))



# def add_value():  # essa function faz EXATAMENTE 1 ÚNICA COISA, o que é ótimo....
#     blockchain.append([get_last_blockchain_value(), 5.3])
#     print(blockchain)



def add_value(transaction_amount, last_transaction=[1]):  # essa function usa DEFAULT PARAMETERS....
    """Faz append de um novo value, assim como o value do ÚLTIMO BLOCKCHAIN, à blockchain global do arquivo
    
        Arguments:
    :transaction_amount: The amount that should be added.
    :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)



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


add_value(get_user_input(), [1])





add_value(0.9, get_last_blockchain_value())

# input_amount = float(input('Please enter the value of your transaction: '))




add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=get_user_input())  #EXEMPLO DE ___ 'KEYWORD ARGUMENTS' dentro de nossos calls (ou seja, DEIXAMOS DE LADO AQUELA 'IMPORTÂNCIA DA ORDEM' na call de nossas functions...) -> ESSA FUNCTION TERÁ O MESMO EFEITO DAQUELA DE CIMA, MAS COM UMA SINTAXE DIFERENTEZINHA....

# input_amount = float(input('Please enter the value of your transaction: '))


add_value(transaction_amount=get_user_input())

# input_amount = float(input('Please enter the value of your transaction: '))


add_value(get_user_input(), get_last_blockchain_value())

# input_amount = float(input('Please enter the value of your transaction: '))

add_value(get_user_input(), get_last_blockchain_value())



