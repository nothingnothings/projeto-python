



from wallet import Wallet


import json


from uuid import uuid4




from blockchain14MODULESETPPS import Blockchain


# from util.fileRelated import FileAccess ##imports todos AGRUPADOS, em uma mesma PACKAGE ('util')...

from util.utility2 import Utility


OWNER = 'Arthur'







class Node:
    """THE NODE WHICH RUNS THE LOCAL BLOCKCHAIN INSTANCE"""





    

    def __init__(self):
        # self.id = uuid4()
        # self.id = 'MAX' ##provisório
        # print(self.id)
        # self.id = 'MAX'
        self.message = ''
        self.wallet = Wallet() #### a wallet inicialmente nÃO TERÁ COISA ALGUMA, pq o user ainda não decidiu se quer CARREGAR UMA WALLET QUE JÁ EXISTIA, ou se então quer 'COMEÇAR DO 0', com uma NOVA WALLET...

        # self.blockchain = Blockchain(self.id)
        # self.blockchain = Blockchain(self.wallet.public_key)
        self.blockchain = None





    def listen_for_input(self, blockchain):
        waiting_for_input = True

        while waiting_for_input:


            if (self.blockchain == None):
                print('No wallet loaded')
                print('c: Create a new wallet')
                print('l: Load an existing wallet')
                user_input = self.get_user_choice()
                if(user_input == 'c'):
                    # self.create_wallet()
                    # wallet = Wallet()  ###vai criar NOVA WALLET, vazia...]
                    print("""Warning: creating a new wallet will overwrite contents in the wallet.txt file.

Proceed(Y/N)?
""")
                    answer = input('Your choice: ')
                    if (answer.lower() == 'y'):
                        self.wallet.create_keys()
                        self.blockchain = Blockchain(self.wallet.public_key)
                        self.message = "A new wallet was created."
                    elif(answer.lower() == 'n'):
                        print('')

                    # self.wallet.create_keys()
                elif(user_input == 'l'):
                    if (self.wallet.load_keys() == False):
                        self.wallet.create_keys()
                        self.blockchain = Blockchain(self.wallet.public_key)
                        self.message = "A new wallet was created."
                    else:
                        self.blockchain = Blockchain(self.wallet.public_key)
                        self.message = """Your wallet was loaded.
    """


                
            else:
                print('-' * 30)
                print('1: Add a new transaction value')
                print('2: Display current blockchain')
                print('3: Show participants')
                print("b: Show user's balance")
                # print('c: Recreate wallet')
                print('h: Manipulate the chain')
                print('l: Load another wallet')
                print('m: Mine a block')
                print('q: Quit the program')
                print('s: Show current loaded wallet')
                print('v: Verify open transactions')
                print('-' * 30)
                print('')
                print(self.message)
                print('')
                user_input = self.get_user_choice()
                if(user_input == '1'):
                    # user_transaction = self.get_transaction_value(self.id)

                    if (self.wallet.public_key == None):
                        self.message = 'No public key detected. Please load in a valid wallet before trying to add a transaction.'
                    else:
                        user_transaction = self.get_transaction_value(self.wallet.public_key)

                        if(user_transaction == None):
                            # print(
                            #     'Please enter a valid sender, recipient and transaction value.')
                            self.message = 'Please enter valid sender, recipient and transaction values.'
                        else:
                            sender, recipient, amount = user_transaction

                            signature = self.wallet.sign_transaction(amount, recipient, self.wallet.public_key)

                            if self.blockchain.add_transaction(sender, recipient, signature, amount):

                                # print('Added transaction!')
                                self.message = 'Added transaction!'
                            else:
                                # print('Transaction failed')
                                self.message = 'Transaction failed to be added.'

                elif(user_input == '2'):
                    self.output_blockchain()
                elif(user_input == 'q'):
                    waiting_for_input = False
                # elif(user_input == 'c'):
                # elif(user_input == 'c' and self.blockchain == None):
                #     print('WARNING: ')
                #     # self.create_wallet()
                #     # wallet = Wallet()  ###vai criar NOVA WALLET, vazia...]
                #     self.wallet.create_keys()
                #     self.blockchain = Blockchain(self.wallet.public_key)
                #     self.message = "A new wallet was created"

                    # self.wallet.create_keys()

                elif(user_input == 'l'):
                    self.wallet.load_keys()
                    self.message = "Your wallet was loaded "
                    
    # Private key: {self.wallet.private_key}

    # Public key: {self.wallet.public_key}

    # """
                

                elif(user_input == 'h'):
                    print(self.blockchain)
                    elementIndex = input(
                        'Enter the number of the element you want to manipulate: ')
                    if (elementIndex.isnumeric()):
                        if (len(self.blockchain) >= int(elementIndex) + 1):
                            elementValue = input(
                                ' Please Enter the value you want to insert: ')
                            chain = self.blockchain.get_chain()

                            chain[int(elementIndex)]['processed_transactions'] = [
                                {'sender': 'test', 'recipient': 'tested', 'amount': 1212}]
                        else:
                            # print(
                            #     'No block for that index, please insert sufficient number of blocks before trying to manipulate a specific one')
                            self.message = 'No block for that index, please insert sufficient number of blocks before trying to manipulate a specific one'
                    else:
                        # print('Invalid index entered, please try again')
                        self.message = 'Invalid index entered, please try again'

                elif(user_input == 'm'):
                    # if (self.wallet.verify_transactions(self.blockchain.get_open_transactions()) == False):  ##minha versão do código, que não funciona...
                    #     self.message = 'Invalid transaction detected, exiting app...'
                    #     waiting_for_input = False
                        
                    if (self.wallet.public_key != None):
                            if self.blockchain.mine_block():
                                # print(' MINED')
                                self.message = 'MINED'
                            else:
                                self.message = 'MINING FAILED'
                    else:
                        # print('No public key detected. Please load in a valid wallet')
                        self.message = 'No public key detected. Please load in a valid wallet'


                        # self.blockchain.open_transactions = []

                        # FileAccess.save_data(
                        #     self.blockchain.chain, self.blockchain.get_open_transactions())

                elif(user_input == '3'):
                    print(self.blockchain.participants)
                elif(user_input == 's'):
                    self.message = f"""Private key: {self.wallet.private_key}

Public key: {self.wallet.public_key}
                    
                    """
                elif(user_input == 'b'):
                    sent, received, balance = self.blockchain.get_balance()
                    # print(f'Blocks sent by {self.wallet.public_key}: ' +
                    #       '{sent:>6.2f}'.format(sent=sent))
                    # print(f'Blocks received by {self.wallet.public_key}: ' +
                    #       '{received:>6.2f}'.format(received=received))
                    # print(f'Total Balance of {self.wallet.public_key}: ' +
                    #       '{balance:>6.2f}'.format(balance=balance))

                    self.message = f"""Blocks sent by {self.wallet.public_key}: {sent:>6.2f}

    Blocks received by {self.wallet.public_key}: {received:>6.2f}

    Total balance of {self.wallet.public_key}: {balance:>6.2f}
                """
                elif(user_input == 'v'):

                    if (Utility.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance, Utility.verify_transaction)):
                        # print('Transactions are valid.')
                        self.message = 'Transactions are valid.'

                    elif(Utility.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance, Utility.verify_transaction) == None):
                        # print('No transactions to verify, please add a transaction.')
                        self.message = 'No transactions to verify, please add a transaction.'
                    else:
                        # print('Invalid transactions detected.')
                        self.message = 'Invalid transactions detected.'
                else:
                    # print('-' * 40)
                    # print('Invalid command.')
                    self.message = 'Invalid command.'

                if(not Utility.verify_chain(self.blockchain.chain, Utility.valid_proof)):
                    # print('Blockchain was found invalid.')
                    self.message = 'Blockchain was found invalid.'
                    # print(self.blockchain.get_chain())
                    waiting_for_input = False
                # else:
                #     print('Blockchain is valid')
        else:
                # print('User left')
                    self.message = 'User left.'





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
            # print('TEST')
            return None
        user_transaction_input = (
            user_transaction_sender, user_transaction_recipient, float(user_transaction_amount))
        return user_transaction_input

    def output_blockchain(self):
        """Outputs our blockchain in the terminal"""
            
        self.message = f"""Outputting blockchain:

{self.blockchain.chain}
            """



    # def create_wallet(self): ###lógica transplantada para 'create_keys' e etc, lá em 'wallet.py'...
    #     self.wallet = Wallet(True)
    #     print(self.wallet.private_key, self.wallet.public_key)
    #     with open('wallet.txt', mode="w") as f:
    #         print(self.wallet.private_key)
    #         f.write(str(self.wallet.private_key))
    #         f.write('\n')
    #         f.write(str(self.wallet.public_key))



    
    # def load_wallet(self):
    #     with open('wallet.txt', mode="r") as g:
    #         private_key, public_key = g.readlines()
    #     self.wallet = Wallet(False)
    #     self.wallet.private_key =  private_key
    #     self.wallet.public_key = public_key
    #     print(self.wallet.private_key, self.wallet.public_key)


# new_node = Node()


# new_node.listen_for_input(new_node.blockchain)




if __name__ =='__main__':  ###esse check serve para INTERROMPER NOSSA EXECUÇAÕ DO APP SE FOR _ CONSTATADO QUE ESSE ARQUIVO 'node.py' NÃO FOI O 'STARTER FILE', o arquivo INICIAL DE CÓDIGO QUE __ INICIALIZA TODOS OS OUTROS ARQUVOS....
    new_node = Node()
    new_node.listen_for_input(new_node.blockchain)





 
print(__name__)   ####special DUNDER VARIABLE oferecida pelo python... built-in...  --> vai retornar o value de '__main__', pq o 'node.py' É REALMENTE RESPONSÁVEL pelO START DO FLOW DE NOSSO RUNTIME... (Se naõ fosse, apareceria UM VALUE correspondente ao 'nome do arquivo que chamou esse arquivo node.py' NESSA VARIABLE DE '__name__'..)