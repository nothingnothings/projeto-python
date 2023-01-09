
from uuid import uuid4 ###algoritmo usado para CRIAR UNIQUE IDS....

from utility2 import Utility


from blockchain12comCLASSESEOBJECTS import Blockchain



from fileRelated import FileAccess


OWNER = 'Arthur'


class Node:

    # def __init__(self, blockchain):
    #     self.blockchain = blockchain
    def __init__(self):
        self.id = uuid4()
        print(self.id)
        self.blockchain = Blockchain(self.id)

    def listen_for_input(self, blockchain):
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
            user_input = self.get_user_choice()
            if(user_input == '1'):
                user_transaction = self.get_transaction_value(self.id)

                if(user_transaction == None):
                    print(
                        'Please enter a valid sender, recipient and transaction value.')
                else:
                    sender, recipient, amount = user_transaction
                    if self.blockchain.add_transaction(sender, recipient, amount):
                    # if add_transaction(sender, recipient, amount):
                    # if add_transaction(sender, recipient, amount):
                        print('Added transaction!')
                    else:
                        print('Transaction failed')

            elif(user_input == '2'):
                self.output_blockchain()
            elif(user_input == 'q'):
                waiting_for_input = False

            elif(user_input == 'h'):
                print(self.blockchain)
                elementIndex = input(
                    'Enter the number of the element you want to manipulate: ')
                if (elementIndex.isnumeric()):
                    if (len(self.blockchain) >= int(elementIndex) + 1):
                        elementValue = input(
                            ' Please Enter the value you want to insert: ')
                        chain = self.blockchain.get_chain()
                        # self.blockchain.chain[int(elementIndex)]['processed_transactions'] = [
                        chain[int(elementIndex)]['processed_transactions'] = [
                            {'sender': 'test', 'recipient': 'tested', 'amount': 1212}]
                    else:
                        print(
                            'No block for that index, please insert sufficient number of blocks before trying to manipulate a specific one')
                else:
                    print('Invalid index entered, please try again')

            elif(user_input == 'm'):
                # if mine_block():
                  if self.blockchain.mine_block():
                    print(' MINED')
                    # open_transactions = []
                    self.blockchain.open_transactions = []
                    # código pertinente ---> salva no nosso filesystem, no nosso arquivo 'blockchain.txt', o BLOCKCHAIN E OPEN_tRANSACTIONS ATUAIS..
                    # self.blockchain.save_data()
                    # FileAccess.save_data(self.blockchain.chain, self.blockchain.open_transactions)
                    FileAccess.save_data(self.blockchain.get_chain(), self.blockchain.get_open_transactions())
                    # save_data()
            elif(user_input == '3'):
                print(self.blockchain.participants)
            elif(user_input == 'b'):
                sent, received, balance = self.blockchain.get_balance(self.id)
                print(f'Blocks sent by {self.id}: ' +
                      '{sent:>6.2f}'.format(sent=sent))
                print(f'Blocks received by {self.id}: ' +
                      '{received:>6.2f}'.format(received=received))
                print(f'Total Balance of {self.id}: ' +
                      '{balance:>6.2f}'.format(balance=balance))
            elif(user_input == 'v'):
                # if (verify_transactions()):
                # if (Utility.verify_transactions(open_transactions, get_balance(OWNER))):
                # new_utility = Utility() ##criamos STATIC METHODS nessa class aí, por isso não precisamos instanciar...
                # if (new_utility.verify_transactions(self.blockchain.open_transactions, self.blockchain.get_balance(self.id))):
                if (Utility.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance(self.id), Utility.verify_transaction)):
                    print('Transactions are valid.')
                # elif(verify_transactions() == None):
                # elif(new_utility.verify_transactions(self.blockchain.open_transactions, self.blockchain.get_balance(self.id)) == None):
                elif(Utility.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance(self.id), Utility.verify_transaction) == None):
                    print('No transactions to verify, please add a transaction.')
                else:
                    print('Invalid transactions detected.')
            else:
                print('-' * 40)
                print('Invalid command.')
            # if(not verify_chain()):
            # new_utility = Utility() ##criamos STATIC METHODS nessa class aí, por isso não precisamos instanciar...
            # if(not new_utility.verify_chain(self.blockchain)):
            # if(not Utility.verify_chain(self.blockchain, Utility.valid_proof)):
            if(not Utility.verify_chain(self.blockchain.get_chain(), Utility.valid_proof)):
                print('Blockchain was found invalid.')
                print(self.blockchain.get_chain())
                waiting_for_input = False
            else:
                print('Blockchain is valid')
        else:
            print('User left')

    def get_user_choice(self):
        """ Returns the input of the user (either 1, 2, h or q) to proceed with the options """
        user_input = input('Please choose an option: ')

        return user_input

    def get_transaction_value(self, OWNER):
        """ Returns the input of the user (sender, recipient, amount) as a tuple, to proceed with option 1 """

        user_transaction_sender = OWNER

        user_transaction_recipient = input(
            "Please enter the recipient's name: ")
        if (user_transaction_recipient == '' or not isinstance(str(user_transaction_sender), str)):
            return None
        user_transaction_amount = input('Please enter transaction amount: ')
        if (user_transaction_amount == '' or not user_transaction_amount.isnumeric() or isinstance(user_transaction_amount, bool)):
            print('TEST')
            return None
        user_transaction_input = (
            user_transaction_sender, user_transaction_recipient, float(user_transaction_amount))
        return user_transaction_input

    def output_blockchain(self):
        # for block in self.blockchain.chain:
        for block in self.blockchain.get_chain():
            print('Outputting block')
            print(block)











new_node = Node()



new_node.listen_for_input(new_node.blockchain)