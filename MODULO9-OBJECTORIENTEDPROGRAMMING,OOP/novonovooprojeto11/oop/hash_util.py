import hashlib
import json
from collections import OrderedDict


def hash_block(block):
    """Hashes a block and returns a string representation of it"""
    # return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    # converted_block = block.__dict__ ##isso vai CONVERTER NOSSO BLOCK (que é um object) EM UM DICT, PARA QUE ESSE DICT POSSA ENTÃO SER CONVERTIDO EM JSON...
    
    converted_block = block.__dict__.copy() ### é necessário chamar esse '.copy()' sobre esse dict retornado aí..


    converted_block['processed_transactions'] = [transaction.to_ordered_dict() for transaction in converted_block['processed_transactions'] ]
    # print(converted_block, 'LINE541251')

    return hash_string_256(json.dumps(converted_block, sort_keys=True).encode())






def hash_string_256(string):
    # print(string, 'LINE')
    return hashlib.sha256(string).hexdigest()


# ###precisa retornar TRUE/FALSE (o hash precisa ter número de 0s inicial compatível com o que definimos para nosso app... esse é o proof of work)...
# def valid_proof(transactions, previous_block_hash, proof): 


#     # guess = (str(transactions) + str(previous_block_hash) + str(proof)).encode()

#     # ordered_transactions = []

#     # for transaction in transactions:
#     #     ordered_transaction = OrderedDict([('amount', transaction.amount), ('recipient', transaction.recipient) , ('sender', transaction.sender)])
#     #     ordered_transactions.append(ordered_transaction)
#     # guess = (str(transactions) + str(previous_block_hash) + str(proof)).encode()


#     ordered_transactions = [transaction.to_ordered_dict() for transaction in transactions]


#     verifiable_transactions = json.dumps(ordered_transactions)



#     # guess = (str(ordered_transactions) + str(previous_block_hash) + str(proof)).encode()


#     guess = (str(verifiable_transactions) + str(previous_block_hash) + str(proof)).encode()

#     # esse hash deverá ter os PRIMEIROS 5 CARACTERES ( ou mais) como 0....
#     # guess_hash = hashlib.sha256(guess).hexdigest()
#     guess_hash = hash_string_256(guess)
#     # if str(guess_hash).startswith('00000', 0): #meio alternativo.
#     #     return guess_hash
#     # else:
#     #     return False
#     # print(guess_hash)
#     return guess_hash[0:4] == '0000'




















# ---> tipo assim:






# hashable_block = block.__dict__.copy()








# mas pq isso?





# acho que entendi... --> é pq 




# 'block.__dict__' 


# VAI RETORNAR UM __ DICT___...



# -----> E DICTS_ _ SÃO _ REFERENCE TYPES.... -----> 



# isso quer dizer que quando essa function for EXECUTADA DE NOVO,

# E O CÓDIGO 

# DE 


# 'hashable_block = block.__dict__' 



# FOR EXECUTADO DE NOVO,



# o 'block.__dict__' 


# armazenado 

# nessa variable 

# SEMPRE VAI __ ACABAR 



# SE


# REFERINDO AO 



# ''CURRENT block.__dict__'''


# e 

# ao 

# 'OLD block.__dict__' 


# AO  MESMO TEMPO....





# -->  SE VOCê NÃO FIZER ESSAS COPIES, O QUE ACONTECERÁ 


# É QUE 



# vocÊ acabará com 

# hashes não 
# funcionando 


# bem juntos, pq 




# você estará MUDANDO DE FORMA INVISÍVEL DICTS ANTIGOS, de outros blocks...







# ------->  É POR ISSO QUE QUEREMOS CRIAR UMA NOVA COPY,


# UM NOVO DICTIONARY,



# TODA VEZ QUE 


# HASHEAMOS UM NOVO BLOCK...