import json



from block import Block 



from transaction import Transaction




class FileAccess:

    chain = []


    @staticmethod
    def load_data(chain, open_transactions):
        # global blockchain  ##agora essas variables serão INTERNAS a 'Blockchain'..
        # global open_transactions
        try:
            with open('blockchain.json', mode='r') as g:
                file_content = g.readlines()
                chain = json.loads(file_content[0][:-1])
                updated_blockchain = []
                for block in chain:
                    # converted_tx = [Transaction(tx['amount'], tx['recipient'], tx['sender']) for tx in block.processed_transactions]
                    converted_tx = [Transaction(tx['amount'], tx['recipient'], tx['sender']) for tx in block['processed_transactions']]
                    # converted_tx = [Transaction(tx['amount'], tx['recipient'], tx['sender']) for tx in block['processed_transactions']]
                    updated_block = Block(block['previous_block_hash'], block['index'], converted_tx, block['proof'], block['timestamp'])
                    # updated_block = Block(block.previous_block_hash, block.index, converted_tx, block.proof, block.timestamp)
                    updated_blockchain.append(updated_block)
                chain = updated_blockchain ###uso de um setter (ver código lá de 'blockchain13')....
                open_transactions = json.loads(file_content[1])

                updated_transactions = []
        
                for tx in open_transactions:
                    updated_transaction = Transaction(tx['amount'], tx['recipient'], tx['sender'])

                    updated_transactions.append(updated_transaction)
                open_transactions = updated_transactions

        except(IOError, IndexError):
            print('Handled exception...')
            # GENESIS_BLOCK = Block('', 0, [], 100, 0)  
            # self.chain = [GENESIS_BLOCK]  ##código desnecessário, pq agora será TRANSPLANTADO LÁ PARA o '__init__()' (vamos INICIALIZAR NOSSA BLOCKCHAIN LÁ... SE UMA BLOCKCHAIN NÃO EXISTIR, ESSA LÓGICA ALI DE BAIXO _ VAI __o CRIAR, com '[genesis_block]' no seu interior... -> esse value de '[genesis_block]' vai ser OVERWRITTADO quando forem minerados mais blocks, por meio da function de 'load_data'...)
            # self.open_transactions = []
        finally:
            print('Your data was or was not loaded. See error statements')
            print('clean-up work')



    @staticmethod
    def save_data(chain, open_transactions): ## para o save de nossa data, nesse caso concreto, a 'ORDER DE NOSSAS DICTS' não interessa, pq só vamos ARMAZENAR AS TRANSACTIONS EM UM ARQUIVO JSON, e não 'checar a validade' de nossa blockchain/transactions (isso é apenas feito lá nos methods de VERIFY, em 'hash_util.py')...
        """Saves the data of the blockchain in a file in your system's storage"""
        try:
            # with open('blockchain.txt', mode='w') as f:
            with open('blockchain.json', mode='w') as f:
                # f.write(str(blockchain))  #vai writtar essa LIST como um value de STRING no seu arquivo de texto.... --> mas não queremos fazer isso, pq é suboptimal... melhor armazenar esses valores como __ JSON_ data...
                # print(open_transactions)
                # print(open_transactions)
                # converted_transactions = []

                # for transaction in open_transactions:
                #     converted_transactions.append(Transaction(transaction['amount'], transaction['recipient'], transaction['sender']))
                # converted_transactions = [transaction.__dict__ for transaction in converted_transactions]
                ##mesma coisa que isto:
                # converted_transactions = [Transaction(transaction['amount'], transaction['recipient'], transaction['sender']).__dict__ for transaction  in open_transactions]

                # converted_transactions = [tx.__dict__ for tx in open_transactions]
                converted_transactions = [tx.__dict__ for tx in open_transactions]


                # converted_blockchain = [] ### meu código, que não funcionou...
                # for block in blockchain:
                #     # não é necessário '.__dict__.copy()' aqui pQ NÃO VAMOS MANIPULAR ESSE DICT (situação diferente daquela vista em 'hash_block', pq lá VAMOS MANIPULAR NOSSO DICT)....
                #     converted_blockchain.append(block.__dict__) ###vai converter todos nossos 'block' (formato OBJECT 'BLOCK') em DICTS, dicts que então poderemos usar naquele CONVERSOR JSON (pq as DICTS são compatíveis com a conversão para json, ao passo que 'objects', não)...
                

                
                # for block in converted_blockchain:
                #     dict_transactions = []
                #     for transaction in block['processed_transactions']:
                #         # dict_transactions.append(transaction.to_ordered_dict())
                #         dict_transactions.append(transaction.__dict__)
                #     block['processed_transactions'] = dict_transactions

                #código do professor...  --> o objetivo desse código era CONVERTER AO MESMO TEMPO OS BLOCKS E AS TRANSACTIONS (dentro de cada um desses block objects) EM DICTS...
                # converted_blockchain = [block.__dict__ for block in [ Block(block_el.previous_block_hash, block_el.index, [tx.__dict__ for tx in block_el.processed_transactions], block_el.proof, block_el.timestamp) for block_el in blockchain ]  ] ##'block_el' é originalmente um OBJECT.... por isso a refeerncia a seus valores, nessa list comprehension,... --> queremos converter TANTO OS OBJECTS 'Block' como 'Transacion' EM __ DICTS__, PARA QUE POSSAM SER ARMAZENADOS COMO JSON DATA EM ARQUVIOS JSON/TEXT...
                converted_blockchain = [block.__dict__ for block in [ Block(block_el.previous_block_hash, block_el.index, [tx.__dict__ for tx in block_el.processed_transactions], block_el.proof, block_el.timestamp) for block_el in chain]  ] ##'block_el' é originalmente um OBJECT.... por isso a refeerncia a seus valores, nessa list comprehension,... --> queremos converter TANTO OS OBJECTS 'Block' como 'Transacion' EM __ DICTS__, PARA QUE POSSAM SER ARMAZENADOS COMO JSON DATA EM ARQUVIOS JSON/TEXT...
                

                for block in converted_blockchain:
                    for transaction in block['processed_transactions']:
                        transaction['sender'] = str(transaction['sender'])

                for transaction in converted_transactions:
                    transaction['sender'] = str(transaction['sender'])


                f.write(json.dumps(converted_blockchain))
                f.write('\n') #line break entre linhas de info...
                f.write(json.dumps(converted_transactions))
        except IOError: 
            print('Saving failed!')



