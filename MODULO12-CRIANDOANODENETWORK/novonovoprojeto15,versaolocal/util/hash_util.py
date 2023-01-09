"""contains import of 'hashlib', for creating random hashes that are used 
in the verification of our blockchain (security mechanism built upon the comparison 
between current and last block)"""

                        ###essa sintaxe é RUIM, prefira a do '__all__ = []', que é mais efetiva para cONTROLAR QUAIS COISAS DEVEM SER EXPORTADAS....
# import hashlib as _h1  ####QUANDO ESCREVEMOS com '_' no início, dizemos ao python que ESSE ARQUIVO NÃO DEVE SER EXPORTADO COM OS OUTROS,, QUANDO exportarmos esse module/arquivo de 'hash_util.py'
# import json
# from collections import OrderedDict  





import hashlib
import json
from collections import OrderedDict





__all__ = ['hash_block', 'hash_string_256']  ###COISAS QUE DEVERÃO SER PERMITIDAS COMO 'exports' desse arquivo 'hash_util.py'...


def hash_block(block):
    """Hashes a block and returns a string representation of it"""

    converted_block = block.__dict__.copy()

    converted_block['processed_transactions'] = [transaction.to_ordered_dict(
    ) for transaction in converted_block['processed_transactions']]

    return hash_string_256(json.dumps(converted_block, sort_keys=True).encode())


def hash_string_256(string):

    return hashlib.sha256(string).hexdigest()
