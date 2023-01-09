"""Provides verification helper methods"""   ###DOCSTRING (é usado para COMENTAR O QUE UM DETERMINADO ARQUIVO/MODULE FAZ)....

import json

# from hash_util import hash_string_256, hash_block

from util.hash_util import hash_string_256, hash_block   ##vamos importar DESSE MESMO MÓDULO AÍ.. ('util')..

from wallet import Wallet

from functools import reduce



__all__ = ['Utility']

class Utility:

    @staticmethod
    def verify_chain(blockchain, valid_proof):

        for(index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_block_hash != hash_block(blockchain[index - 1]):
                return False

            if not valid_proof(block.processed_transactions[:-1], block.previous_block_hash, block.proof):
                print('Proof of work is invalid.')
                return False
        return True

    @staticmethod
    def verify_transaction(transaction, get_balance, check_funds=True):  ##só não checará os 'funds'/balance do USER em relaçaõ ao amount da given transaction _ NO CASE DO 'verify_transactions', em que ESSA INFO DO BALANCE NÃO INTERESSA (e em que APENAS A validade da 'signature' em uma transaction vai interessar)....
        
        if (not check_funds):
            return Wallet.verify_transaction(transaction)

        # sender_balance = get_balance(transaction.sender)[2]
        sender_balance = reduce(lambda x,y: x+y, get_balance())
        print(sender_balance, float(transaction.amount))

        # print(sender_balance)
        return (sender_balance >= float(transaction.amount)) and Wallet.verify_transaction(transaction)




    @staticmethod
    def verify_transactions(open_transactions, get_balance, verify_transaction):
        return all([verify_transaction(transaction, get_balance, False) for transaction in open_transactions])

    @staticmethod
    def valid_proof(transactions, previous_block_hash, proof):

        ordered_transactions = [transaction.to_ordered_dict()
                                for transaction in transactions]

        verifiable_transactions = json.dumps(ordered_transactions)

        guess = (str(verifiable_transactions) +
                 str(previous_block_hash) + str(proof)).encode()

        guess_hash = hash_string_256(guess)
        print(guess_hash) ##mostra o progresso do 'mine'...

        return guess_hash[0:4] == '0000'
