from argparse import ArgumentParser
# --> 'argparse'# É IMPORTADO LÁ DA PACKAGE __ STANDARD_ DO PYTHON 'ArgumentParser'...

# --> e o 'argparse'


# É UMA __ FERRAMENTA__ QUE __ 


# NOS PERMITE __ PARSEAR___ 

# OS ARGUMENTOS __ 


# QUE PASSAMOS 

# COM NOSSO 'python filename.py xxxx'....





from flask import Flask, jsonify ##jsonify é usado para CONVERTER DATA (como dicts) EM __ JSON DATA__, que então é RETORNADA AO USER/CLIENT....


from flask import request ####OUTRA COISA BOA IMPORTADA DO FLASK, NOS AJUDA _ A EXTRAIR__ DATA DE REQUESTS DE TIPO POST (do body, por exemplo)....


# from flask import send_file ## não é utilizado para enviar HTML PQ É MAIS INSEGURO DO QUE O 'send_from_directory'....





from flask import send_from_directory



from flask_cors import CORS, cross_origin #usado para RESOLVER PROBLEMAS DE CORS....


from blockchain14MODULESETPPS import Blockchain


from wallet import Wallet

app = Flask(__name__)  ##devemos criar nosso APP FLASK, que vai nos permitir receber requests e enviar responses....
                        ##o argumento '__name__' (special variable) é usado para INFORMAR AO FLASK __ SOBRE __ 'EM QUE CONTEXT ELE DEVERÁ SER EXECUTADO'... -> é uma informação importante...

# wallet = Wallet()   ###queremos ter uma Wallet LOGO DE INÍCIO...  OBS: só o call de 'Wallet()' não nos entrega private e public keys, precisamos de outros methods para isso...

# blockchain = Blockchain(wallet.public_key)  ##inicializa nossa blockchain ao mesmo tempo que é passada a 'public_key' da wallet que criamos/loadamos...

CORS(app)




@app.route('/wallet', methods=['POST'])
def create_keys():
    if (wallet.create_keys()):
        global blockchain
        blockchain = Blockchain(wallet.public_key, port)
        response = {
        'public_key': wallet.public_key,
        'private_key': wallet.private_key,
        'funds': blockchain.get_balance()[2]
        }
        return jsonify(response), 201

    response = {
            'message': 'Failed to create wallet.'
        }
    return jsonify(response), 500





@app.route('/wallet', methods=['GET'])
def load_keys():
    if (wallet.load_keys()):
 
            global blockchain
            blockchain = Blockchain(wallet.public_key, port)
            response = {
                'public_key': wallet.public_key,
                'private_key': wallet.private_key,
                'funds': blockchain.get_balance()[2]
                }
            return jsonify(response), 201

    response = {
            'message': 'Failed to load existing wallet. Loading new wallet...',
            'public_key': wallet.public_key,
            'private_key': wallet.private_key,
            'funds': 0
           
            
        }
    return jsonify(response), 500



@app.route('/funds', methods=['GET'])
def get_balance():
    if (wallet.public_key != None):
        user_balance = blockchain.get_balance()
        print(user_balance)
        response = {
            'message': 'Balance successfuly retrieved',
            'Funds sent':  user_balance[0],
            'Funds received': user_balance[1],
            'Total funds': user_balance[2]
        }
        return jsonify(response), 200
    else:
        response = {
            'message': 'Failed to retrieve your balance',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500



@app.route('/', methods=['GET'])  ### É ASSIM QUE DEFINIMOS 'ROUTES' no nosso APP FLASK (bem parecido com o NODEEXPRESS SERVER)...
def get_ui():
    # return 'This works!'
    # send_file('exemploDeBoostrap.html') não funciona (preciso construir o path)..
    # curr_dir = Path(__file__).parent ## estes códigos NÃO FUNCIONAM.... (e 'send_file' é mt inseguro para ser usado para enviar htmlll)
    # file_path = curr_dir.joinpath('exemploDeBoostrap.html')
    # print(file_path)
    # send_file(file_path)
    return send_from_directory('ui', 'exemploDeBootstrap.html')





@app.route('/network', methods=['GET'])
def get_network_ui():
    print('LOADED')
    return send_from_directory('ui', 'network.html')






@app.route('/chain', methods=['GET'])
def get_chain():
    if (not wallet.public_key != None):
        # response = {'message': 'Failed to retrieve blockchain. Please ensure that a wallet is loaded.',
        #             'wallet_set_up': False}

        # return jsonify(response), 200
        return 'Please ensure that a wallet was loaded.', 403


    chain_snapshot = blockchain.chain
    dict_chain = [block.__dict__.copy() for block in chain_snapshot]
    for dict_block in dict_chain:
        dict_block['processed_transactions'] = [tx.__dict__ for tx in dict_block['processed_transactions']]
    print(dict_chain)
    return jsonify(dict_chain), 200




@app.route('/mine', methods=['POST'])
def mine_block():
    
    print(wallet.public_key, 'LINE')
    if (not blockchain.mine_block() or wallet.public_key == None):
        response = {
            'message': 'Failed to mine a block. Ensure that you have a wallet, and valid transactions in your blocks.',
            'wallet_set_up': wallet.public_key != None
        }
        return jsonify(response), 500 ### erro padrão..

    block = blockchain.chain[-1].__dict__.copy()
    block['processed_transactions'] = [tx.__dict__ for tx in block['processed_transactions']]

    chain_snapshot = blockchain.chain
    dict_chain = [block.__dict__.copy() for block in chain_snapshot]
    for dict_block in dict_chain:
        dict_block['processed_transactions'] = [tx.__dict__ for tx in dict_block['processed_transactions']]
    
    response = {
        'message': 'Block added successfully.',
        'added_block': block,
        'blockchain': dict_chain, ####
        'funds': blockchain.get_balance()[2]
    }
    return jsonify(response), 201


@app.route('/broadcast-transaction', methods=['POST'])
def broadcast_transaction():
    print('ENTERED')
    values = request.get_json()
    if not values:
        response = {'message': 'No data found.'}
        return jsonify(response), 400

    required = ['sender', 'recipient', 'amount', 'signature']
    if (not all(field in values for field in required)):
        response = {'message': 'The request is missing important data.'}
        return jsonify(response), 400
    
    success = blockchain.add_transaction(values['sender'], values['recipient'], values['signature'], values['amount'], True)
    
    if success: 
        response = {
        'message': 'A new transaction was added.',
        'transaction': {
            'sender': values['sender'],
            'recipient': values['recipient'],
            'amount': values['amount'],
            'signature': values['signature']
        },
    }
        return jsonify(response), 200
    else: 
        response = {
            'message': 'Creating a transaction failed'
        }
        return jsonify(response), 500
    




@app.route('/transactions', methods=['GET'])
def get_open_transactions():

    if (wallet.public_key != None):
        response = {
        'transactions': [transaction.__dict__ for transaction in blockchain.get_open_transactions()]
        }
        print(response)
        return jsonify(response), 200
    
    return 'Please ensure that a wallet was loaded.', 403







@app.route('/transaction', methods=['POST'])
def add_transaction():
    if (wallet.public_key != None):
        values = request.get_json()  ### a data precisa estar em formato json para que esse method funcione  --> e values será um DICTIONARY...
        required_fields = ['recipient', 'amount']  ##ESSES FIELDS DEVEM EXISITR DENTRO DO REQUEST ENVIADO PELO USER(a transaction em si) PARA QUE ELE SEJA CONSIDERADO VÁLIDO....
        if not values:
                response = {'message': 'No JSON data attached to request'}
                return jsonify(response), 400
        if (not all(field in values for field in required_fields)):  #com isso, checamos se aqueles keynames em 'required_fields' EXISTEM NO INTERIOR DOS FIELDS dentro de 'values' (dict obtido através de 'request.get_json()')....
            response = {
                'message': 'Required data is missing'
            }
            return jsonify(response), 400
        ### se passamos por esse if checks, já ficamos com A DATA de 'sender', 'recipient' e 'amount' válida dentro de 'values'...
        signature = wallet.sign_transaction(values['amount'], values['recipient'], wallet.public_key)
        # if (not blockchain.add_transaction(wallet.public_key, values['recipient'], signature, values['amount'])):
        #     response = {
        #         'message': 'Failed to add transaction. Please ensure that your wallet was loaded and that you have sufficient funds.',
        #         'wallet_set_up': wallet.public_key != None
        #     }
        #     return jsonify(response), 500


        success = blockchain.add_transaction(wallet.public_key, values['recipient'], signature, values['amount'])
        if success:
            funds = blockchain.get_balance()
            response = {
                'message': 'Successfully added transaction.',
                # 'transactions': blockchain.get_open_transactions().__dict__,
                'transactions': [transaction.__dict__ for transaction in blockchain.get_open_transactions()],
                'added_transaction': {
                    'sender': wallet.public_key,
                    'recipient': values['recipient'],
                    'amount': values['amount'],
                    'signature': signature,
                    'funds': {
                        'sent': funds[0],
                        'received': funds[1],
                        'total': funds[2]
                    }
                }
        }
            return jsonify(response), 201
        else: 
            response = {
                'message': 'Creating a transaction failed.',
                'wallet_set_up': wallet.public_key != None
            }
            return jsonify(response), 500


@app.route('/network/node', methods=['POST'])
def add_node():

    # if (not wallet.public_key != None):
    #     return 'Please ensure that a wallet was loaded.', 403

    values = request.get_json()


    if (not values):
        response = {
            'message': 'No data attached.'
        }
        return jsonify(response), 400
    if ('node' not in values):
        response = {
            'message': 'No node detected in the request.'
        }
        return jsonify(response), 403
    # node = values.get('node') ##mesma coisa que o código de baixo...
    node = values['node']



    if (not node.startswith('localhost:') or not node.split(':', 2)[1].isnumeric() ):
        response = {
            'message': 'Invalid node pattern. Please include "localhost:" at the beginning and ensure that you are inputting a valid number.'
        }
        return jsonify(response), 403




    blockchain.add_peer_node(str(node)) ##isso poderá ser feito _ MESMO __ SEM TENDO UMA WALLET inicialmente...
    
    nodes = blockchain.get_peer_nodes() ## isso será uma list/array....
    response = {
        'message': 'Node added successfully.',
        'all_nodes': nodes
    }
    return jsonify(response), 201


@app.route('/network/node/<nodeId>', methods=['DELETE'])  ##é assim que escrevemos SEGMENTOS DINÂMICOS NO FLASK...
def remove_node(nodeId): #o segmento dinâmico é repassado nessa function/route..


    # if (not wallet.public_key != None):
    #     # response = {'message': 'Failed to retrieve blockchain. Please ensure that a wallet is loaded.',
    #     #             'wallet_set_up': False}

    #     # return jsonify(response), 200
    #     return 'Please ensure that a wallet was loaded.', 403
    print('LINE')

    query_param = nodeId
    print(query_param, 'LINE')

    if (query_param == '' or query_param == None):
        response = {
            'message': 'No nodeId attached to url.'
        }
        return jsonify(response), 400



    
    blockchain.remove_peer_node(query_param)
    print(blockchain.get_peer_nodes(), 'NODES')
    nodes = blockchain.get_peer_nodes()

    response = {
        'message': 'Node removed successfully.',
        'all_nodes': nodes
    }

    return jsonify(response), 200


@app.route('/network/nodes', methods=['GET'])
def get_nodes():


    # if (not wallet.public_key != None):
    #     # response = {'message': 'Failed to retrieve blockchain. Please ensure that a wallet is loaded.',
    #     #             'wallet_set_up': False}

    #     # return jsonify(response), 200
    #     return 'Please ensure that a wallet was loaded.', 403

    nodes = blockchain.get_peer_nodes()


    if (nodes == None):
        response = {
            'message': 'Something went wrong'
        }
        return jsonify(response), 400


    if (not nodes):
        response = {
            'message': 'No nodes found, please add a new node.'
        }
        return jsonify(response), 400
    
    response = {
        'message': 'Nodes successfully retrieved',
        'all_nodes': nodes
    }
    return jsonify(response), 200






if __name__ == '__main__':    ##queremos que esse 'node.py' SEJA EXECUTADO DIRETAMENTE, E NÃO QUE SEJA IMPORTADO...  ##se essa condição é satisfeita, startamos nosso server...
    parser = ArgumentParser() ##standard python library....
    parser.add_argument('-p', '--port', type=int, default=5000) ### ex: python node.py --port 3000  ( o default, caso vocÊ não passe nada, é a porta/argumento de '5000')...
    
    args = parser.parse_args()
    port = args.port  ##retrieva a key de 'port' dentro do objeto 'args' que produzimos com aquele method ali...

    print(args)
    # app.run(host="0.0.0.0", port=5000) 


    wallet = Wallet(port)   ###queremos ter uma Wallet LOGO DE INÍCIO...  OBS: só o call de 'Wallet()' não nos entrega private e public keys, precisamos de outros methods para isso...

    blockchain = Blockchain(wallet.public_key, port)  ##inicializa nossa blockchain ao mesmo tempo que é passada a 'public_key' da wallet que criamos/loadamos...


    app.run(host="0.0.0.0", port=port)  ##0.0.0.0 é um placeholder... significa 'localhost'... 
                # 1o argumento : o ip EM QUE QUEREMOS RODAR O SERVER....
                # 2o argumento: PORTA EM QUE QUEREMOS  FAZER LISTEN


