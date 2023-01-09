import hashlib
import json


def hash_block(block):
    """Hashes a block and returns a string representation of it"""
    # return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
    hash_string_256(json.dumps(block, sort_keys=True).encode())




def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()


###precisa retornar TRUE/FALSE (o hash precisa ter número de 0s inicial compatível com o que definimos para nosso app... esse é o proof of work)...
def valid_proof(transactions, previous_block_hash, proof): 
    guess = (str(transactions) + str(previous_block_hash) + str(proof)).encode()
    # esse hash deverá ter os PRIMEIROS 5 CARACTERES ( ou mais) como 0....
    # guess_hash = hashlib.sha256(guess).hexdigest()
    guess_hash = hash_string_256(guess)
    # if str(guess_hash).startswith('00000', 0): #meio alternativo.
    #     return guess_hash
    # else:
    #     return False
    print(guess_hash)
    return guess_hash[0:4] == '0000'