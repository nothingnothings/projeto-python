
# from util.fileRelated import FileAccess


from functools import reduce ###standard library do python

# from util.hash_util import hash_block 


import json  ###standard library do python




# from requests import post, get ###  não faz parte da standard library do python  --> te deixa te fazer O SEND DE HTTP REQUEST dentro de seu app python (e o destino pode ser qualquer coisa, não precisa ser um server python)...


import requests

from block import Block  

from transaction import Transaction


from util.utility2 import Utility

# assim conseguimos AGRUPAR TODOS NOSSOS IMPORTS SOB UMA MESMA 'package'...
from util.hash_util import hash_block



from wallet import Wallet


MINING_REWARD = 10


__all__ = ['Blockchain']


print(__name__)


class Blockchain:

    def __init__(self, hosting_node_id, node_port):
        GENESIS_BLOCK = Block('', 0, [], 100, 0)

        self._chain = [GENESIS_BLOCK]
        self.__open_transactions = []
        self.participants = {'Max'}
        self.__peer_nodes = set()
        self.node_port = node_port
        self.load_data()
        self.hosting_node = str(hosting_node_id)
    
        #   self.__peer_nodes = set()
        # FileAccess.load_data(self.chain, self.__open_transactions)

    @property
    def chain(self):
        # print('GETTER method called')
        return self._chain[:]

    @chain.setter
    def chain(self, val):
        self._chain = val

    def get_open_transactions(self):
        return self.__open_transactions[:]

    def proof_of_work(self):

        last_block = self._chain[-1]
        last_hash = hash_block(last_block)
        proof = 0

        while not Utility.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof


    def load_data(self):
        """Initialize blockchain + open transactions data from a file."""
        try:
            print(self.node_port, 'LINE')
            with open(f'blockchain-{self.node_port}.json', mode='r') as f:
                # file_content = pickle.loads(f.read())
                file_content = f.readlines()
                # blockchain = file_content['chain']
                # open_transactions = file_content['ot']
                blockchain = json.loads(file_content[0][:-1])
                # We need to convert  the loaded data because Transactions should use OrderedDict
                updated_blockchain = []
                for block in blockchain:
                    converted_tx = [Transaction(
                        tx['amount'], tx['recipient'], tx['signature'], tx['sender']) for tx in block['processed_transactions']]
                    updated_block = Block(
                        block['previous_block_hash'], block['index'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)
                self.chain = updated_blockchain
                open_transactions = json.loads(file_content[1])
                # We need to convert  the loaded data because Transactions should use OrderedDict
                updated_transactions = []
                for tx in open_transactions:
                    updated_transaction = Transaction(
                        tx['amount'], tx['recipient'], tx['signature'], tx['sender'])
                    updated_transactions.append(updated_transaction)
                self.__open_transactions = updated_transactions

                print(file_content[2])
                peer_nodes = json.loads(file_content[2])
                self.__peer_nodes = set(peer_nodes)
        except (IOError, IndexError):
            pass
        finally:
            # print('Cleanup!')
            print('')

    def save_data(self):
        """Save blockchain + open transactions snapshot to a file."""
        try:
            with open(f'blockchain-{self.node_port}.json', mode='w') as f:
                saveable_chain = [block.__dict__ for block in [Block(block_el.previous_block_hash, block_el.index, [
                    tx.__dict__ for tx in block_el.processed_transactions], block_el.proof, block_el.timestamp) for block_el in self.chain]]
                f.write(json.dumps(saveable_chain))
                f.write('\n')
                saveable_tx = [tx.__dict__ for tx in self.__open_transactions]
                for transaction in saveable_tx:
                    transaction['sender'] = str(transaction['sender'])
                f.write(json.dumps(saveable_tx))
                f.write('\n')
                f.write(json.dumps(list(self.__peer_nodes)))  ##writtamos uma LISTA de nossos nodes, contidos dentro do set de 'peer_nodes'...
                

                # save_data = {
                #     'chain': blockchain,
                #     'ot': open_transactions
                # }
                # f.write(pickle.dumps(save_data))
        except IOError:
            print('Saving failed!')



    def get_value(self, person):
        print(self.chain, 'LINE414114')
        print([[transaction.amount for transaction in block.processed_transactions if getattr(transaction, person) == self.hosting_node] for block in self.chain])
        return [[transaction.amount for transaction in block.processed_transactions if getattr(transaction, person) == self.hosting_node] for block in self.chain]


    def get_balance(self, sender=None):
        """Calculate and return the balance for a participant (recipient and sender, both are informed of the balance)."""


        if sender == None: ##entramos nesse block se REALMENTE é o próprio node que add a transaction que terá sua balance calculada por este method....
            if self.hosting_node == None:##ver também a function de 'verify_transaction', lá em 'Utility'..
                return None
            participant = self.hosting_node
        else:  ##entramos nesse block se estamos checando a balance do NODE que __ RECEBE _os funds da transaction...
            participant = sender


        transaction_sender = self.get_value('sender')

        print(transaction_sender, 'LINE2')

        open_transactions_sender = [transaction.amount
                                    for transaction in self.get_open_transactions() if transaction.sender == participant]

        transaction_sender.append(open_transactions_sender)

        # print(transaction_sender[0])

        # print(transaction_sender)

        amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                             if len(tx_amt) > 0 else tx_sum + 0, transaction_sender, 0)

        

        # print(amount_sent)

        transaction_recipient = self.get_value('recipient')

        amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt)
                                 if len(tx_amt) > 0 else tx_sum + 0, transaction_recipient, 0)

        print(amount_received - amount_sent, 'LINEr')
        # print(amount_received)
        return (amount_sent, amount_received, amount_received - amount_sent)





    def mine_block(self):
        """É essa função que PROCESSA NOSSAS OPEN TRANSACTIONS, PARA ENTÃO ADICIONAR UM NOVO BLOCK À BLOCKCHAIN """

        previous_block = self._chain[-1]
        # print(previous_block)

        hashed_block = hash_block(previous_block)
        print(hashed_block)
        print(hashed_block)

        proof = self.proof_of_work()
        print(self.hosting_node, 'HOSTNODE')
        reward_transaction = Transaction(
            MINING_REWARD, self.hosting_node, 'signature', 'ourApp')

        copied_transactions = self.__open_transactions[:]


        for transaction in copied_transactions:
            if (not Wallet.verify_transaction(transaction)):
                self.__open_transactions.remove(transaction)
                return False

        copied_transactions.append(reward_transaction)
        print(copied_transactions, 'COPIED_TRANSACTIONS')
        
        block = Block(hashed_block, len(self._chain),
                      copied_transactions, proof)
        
        
 


        self._chain.append(block)
        self.__open_transactions = []
        self.save_data()

        # FileAccess.save_data(self._chain, self.__open_transactions)
        # FileAccess.save_data(self._chain, copied_transactions)

        # print(self._chain, 'TRIED TO MINE BLOCK')
        return True

    # def add_transaction(self, sender, recipient, amount=1.0):
    def add_transaction(self, sender, recipient, signature, amount=1.0, is_receiving=False):
        """Faz append de uma NOVA TRANSACTION À LIST DE ' open_transactions, e aí RETORNA TRUE OU FALSE, a depender do sucesso de seu códiogo --> verification para ver se o user pode ou naõ realizar essa operação/send de coins...'....

            Arguments:
        :sender: o sender da transaction (nome ou id)   
        :recipient: o receiver da transaction (nome ou id)
        :signature: a SIGNATURE DE CADA TRANSACTION
        :amount: a quantidade (DEVE SER UM FLOAT). DEFAULT É 1.0 coin ...            
        """






        new_transaction = Transaction(amount, recipient, signature, sender)


        # if (not Wallet.verify_transaction(new_transaction)): ##redundante (já temos esse check no method call logo abaixo, de 'Utility')..
        #     return False

        if not Utility.verify_transaction(new_transaction, self.get_balance):
            # print('Your funds are not enough for the chosen operation')
            print('INVALID')
            return False
        else:
            print('VALID')
            self.__open_transactions.append(new_transaction)
            self.participants.add(sender)
            self.participants.add(recipient)
            print(self.__open_transactions)
            
            # FileAccess.save_data(self._chain, self.__open_transactions)
            # FileAccess.save_data(self._chain, self.get_open_transactions())
            self.save_data()

        if (not is_receiving): ## só vamos entrar nesse loop que DISPARA REQUESTS A TODOS OS OUTROS PEER NODES SE __ REALMENTE_ FORMOS _O  'node' ORIGINÁRIO, o node que CRIOU ESSA TRANSACTION AÍ, e que não está só 'RECEBENDO A INFO DE QUE UMA TAL TRANSACTION FOI CRIADA' (como os outros nodes fazem)...
            for node in self.__peer_nodes: ###loop que vai por dentro de TODOS OS PEER NODES para enviar HTTP REQUESTS/info de que nossa transaction foi adicionada, _ A TODOS ELES...
                url = f'http://{node}/broadcast-transition'
                try: #vai 'try' esse disparo de http request específico, dentro do loop
                    response = requests.post(url, json={   ##1o argumento é a url, o segundo é a DATA...  ---> no nosso caso, a data será UM DICT, que será automaticamente convertido em json data por meio desse methjod 'requests.post'...
                                            'sender': sender, 'recipient': recipient, 'amount': amount, 'signature': signature       }  
                                )  
                    if response.status_code == 400 or response.status_code == 500:  ##vamos definir esses status codes de erro LÁ NA NOSSA RESPOSTA DO BACKEND... ('node.py')...
                        print('Transaction declined, resolving needed.')
                        return False
                except requests.exceptions.ConnectionError:
                    continue  ### se esse ERROR DE CONEXÃO (falha de conexão) FOR DETECTADO EM ALGUM DOS NODES, vamos querer simplesmente continuar pq _ EMBORA ESSE NODE TENHA FALHADO, TVZ OUTROS FUNCIONEM... --> ISSO PQ __ A TRANSACTION NÃO FALHOU A VALIDAITON POR SI SÓ, E SIM __ APENAS __ 'NÃO CONSEGUIMOS ENVIAR O REQUEST para esse NODE ESPECÍFICO' -> mas ainda vamos querer continuar disparando requests para os outros nodes...

            return True
    
    def add_peer_node(self, node):
        """Adds a new node to the peer node set.
        
        Arguments:
            :node: The node URL which should be added.
        """

        self.__peer_nodes.add(node)   ##'.add()' é um method que existe DENTRO DE SETS...
        self.save_data()

    def remove_peer_node(self, node):
        """Removes a node from the peer node set.
        
        Arguments:
            :node: The node URL which should be removed.
        """
        self.__peer_nodes.discard(node)
        self.save_data() ###salva a updated node list na nossa TEXT FILE...
        print('REMOVED NODES')

    def get_peer_nodes(self):
        """
        Return a list of all connected peer nodes
        """
        return list(self.__peer_nodes) ##criamos uma LIST A PARTIR DE NOSSO 'SET',  e então a retornamos...

    


        


# print(__name__)
