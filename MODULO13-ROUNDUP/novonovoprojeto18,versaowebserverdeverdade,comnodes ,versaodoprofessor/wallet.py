from Crypto.PublicKey import RSA    ###'Crypto' --> é a package de 'Pycrypto'...
                        ##### 'RSA' -> é um ALGORITMO USADO PARA O GENERATE E TRABALHO COM PUBLIC E PRIVATE KEYS...



import Crypto.Random   ###gera um número realmente aleatório, supostamente....


from Crypto.Signature import PKCS1_v1_5 ##algoritmo especial que GERA SIGNATURES... (será usado para o SIGN de nossas transactions)



from Crypto.Hash import SHA256  ##poderíamos usar o 'sha256' do HASHLIB, que é a mesma coisa (mas aqui usamos essa versaõ do pacote do sha256, pq já estamos utilizando esse pacote mesmo)...


import binascii  ###CONVERTS BINARY DATA (such as our keys) INTO ASCII.... (also converts from ASCII to binary, if you so desire) ---> ASCII IS STRINGS or numbers, essentially..











class Wallet:
    # def __init__(self, isNew):  //minha versaõ do código de 'OPTAR POR CARREGAR UMA WALLET JÁ EXISTENTE OU CRIAR UMA NOVA, DO ZERO'''..s
    #     if (isNew):
    #         self.private_key, self.public_key = self.generate_keys()

    def __init__(self, node_port):
        self.private_key = None
        self.public_key = None
        self.node_port = node_port
        



    def generate_keys(self):
        """CREATES OUR PRIVATE AND PUBLIC KEYS; the public key is built upon the private key, and its job is to identify that its corresponding private_key is in a transaction, valid transaction. 
        As both keys will be produced in binary formats, we convert them to strings using the 'binascii' package """
        
        private_key = RSA.generate(1024, Crypto.Random.new().read) ###quanto maior o número, maior a quantidade de bits e mais segura a key, mas mais tempo demora... ---> quer dizer que esse primeiro parâmetro é a 'LENGTH DE NOSSA KEY'...
        public_key = private_key.public_key()   ###ESSE É UM METHOD __ QUE __ RETORNA/NOS DÁ __ A 'public key' A PARTIR _ DA PRIVATE KEY...  (a public key é NECESSARIAMENTE CRIADA A PARTIR DA PRIVATE KEY)..

        ###binascii.hexlify() -----> É UM METHOD QUE CONVERTE 'binary data' EM REPRESENTAÇÕES HEXADECIMAIS... (É O PRIMEIRO PASSO PARA CONSEGUIRMOS CONVERTER NOSSAS KEYS, QUE ESTÃO EM BINARY DATA FORMAT, em STRINGS)....  

        #### --> é claro que para CONSEGUIRMOS CONVERTER ISSO EM HEXADECIMAL POR MEIO DE 'hexlify', primeiro PRECISAMOS DE BINARY DATA...
        ### as variables de 'public_key' estarão como binary data, sim, mas BD _INACESSÍVEL... --> para conseguirmos acessar essa data, precisamos
        ##precisamos do method '.exportKey()' nessa private_key, que é o METHOD QUE NOS RETORNA A BINARY DATA CONTIDA NESSAS VARIABLES/keys...

        ##mas para conseguirmos essa data binária, precisamos passar o parâmetro de 'format', que diz EM QUAL FORMATO VAMOS QUERER ESSAS KEYS...
         
        ##colocamos 'DER' --> der significa 'BINARY ENCODING'... --> precisamos disso para que o 'hexlify' consiga funcionar... (hexlify converte BINARY DATA EM HEXADECIMAL)..

        ### return (binascii.hexlify(private_key.exportKey(format='DER')))    ###tuple com nossa PRIVATE E PUBLIC KEYS...

        ###finalmente, chamamos '.decode('ascii')' sobre ESSE RESULTADO INTEIRO __ para __ CONSEGUIRMOS CONVERTER ESSA REPRESENTAÇLAÕ _ HEXADECIMAL __ EM ASCII DATA (uma string) QUE REPRESENTA NOSSA KEY... -> é com essa string que trabalharemos...
        
        # return (binascii.hexlify(private_key.exportKey(format='DER'), binascii.hexlify(public_key.exportKey(format='DER'))).decode('ascii')) 
        ### outsourceei esse negócio...
        print(self.convert_binary_to_string(private_key).decode("utf8"), self.convert_binary_to_string(public_key).decode("utf8"))
        return (self.convert_binary_to_string(private_key).decode("utf8"), self.convert_binary_to_string(public_key).decode("utf8"))
        ###ou seja, aqui será RETORNADA UMA _ TUPLE __ COM O FORMATO '(private_key, public_key)', as duas em formato STRING...


    def create_keys(self): ###case de 'começar a wallet do 0'...
         try:
            private_key, public_key = self.generate_keys()
            self.private_key = private_key
            self.public_key = public_key
            with open(f'wallet-{self.node_port}.txt', mode="w") as f:
                # print(self.private_key)
                f.write(str(self.private_key))
                f.write('\n')
                f.write(str(self.public_key))
                return True
         except(IOError, IndexError):
            print('Saving wallet failed!')
            return False
        


    def load_keys(self): 
        try:
            with open(f'wallet-{self.node_port}.txt', mode="r") as g:
                keys = g.readlines()    ###entretanto, precisamos EXCLUIR O 'ÚLTIMO CARACTER' da linha de 'private_key', pq o ÚLTIMO CARACTER É UM LINE BREAK, é '\n'...
            print(keys, 'LINE')
            private_key = keys[0][:-1]   #### com '[:-1]' excluímos o último caracter, que é '\n'....
            public_key = keys[1]
            self.private_key = private_key
            self.public_key = public_key
            # print(self.private_key, self.public_key)
            return True
        except(IOError, IndexError):
            print('Loading wallet failed!')
            print('In the absence of an existing wallet, a new one has been created.')
            self.create_keys()
            return False
            

    def convert_binary_to_string(self, key):
        return binascii.hexlify(key.exportKey(format='DER'))


    def sign_transaction(self, amount, recipient, sender):
        print(self.private_key, 'TEXT')
        signer = PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(self.private_key)))     ###precisamos que nossas KEYS ESTEJAM EM FORMATO BINARY (desconverter elas, que agora estarão armazenadas como STRINGS lá nesse nosso 'wallet', nos attributes)... --> para isso, usamos 'binascii', a package que consegue converter strings em binary data e vice-versa...
        ###unhexlify é o contrário de hexlify --> cnoverte STRINGS DE VOLTA EM BINARY DATA...
        h = SHA256.new((str(amount) + str(recipient) + str(sender)).encode('utf8'))  ##o 'encode('utf8')'  vai CONVERTER NOSSA DATA da transaction (inicialmente STRINGS) em uma BINARY STRING
        ### h é um 'hash'... hash do CONTEÚDO/PAYLOAD DA TRANSACTION....
        signature = signer.sign(h) ## 'signature' vai estar em formato  BINARY, E NAÕ STRING...
        return binascii.hexlify(signature).decode('ascii')  ##assim conseguimos retornar esse value como STRING, e não como BINARY DATA... (chamamos '.decode('ascii')' em cima do '.hexlify()' pq ELE VAI TRANSFORMAR ESSA BINARY DATA EM HEXADECIMAL DATA, que TAM´BEM PRECCISAMOS CONVERTER, por meio de esse '.decode('ascii')'... (que vai transformar isso em uma STRING)...



    # def verify_transactions(self, open_transactions):  ##minha versão do código... 
    #     return all([self.verify_transaction(transaction) for transaction in open_transactions])



    ####MINHA VERSAÕ DO CÓDIGO. CONTÉM ERROS (o verify tem de ser  DA PUBLIC_KEY DENTRO DA TRANSACTION, QUE é 'transaction.sender', e NAÕ DA PUBLIC_KEY QUE TEMOS NA NOSSA WALLET, pq isso n faz sentido)
    # def verify_transaction(self, transaction): ###verifica SE A 'SIGNATURE' dentro de a given transaction é VÁLIDA OU NÃO...
    #     print(binascii.unhexlify(self.private_key))
    #     print(self.public_key)
    
    #     verifier = PKCS1_v1_5.new(RSA.import_key(binascii.unhexlify(self.public_key))) ##O verify sempre se utiliza da PUBLIC KEY, PQ É A PUBLIC KEY que checa se sua SIGNATURE é válida para aquela transaction...

    #     payload_h = SHA256.new((str(transaction.amount) + str(transaction.recipient) + str(transaction.sender)).encode('utf8'))

    #     signature = binascii.unhexlify(transaction.signature)
    
    #     print('VALID')
    #     print(verifier.verify(payload_h, signature))
    #     return verifier.verify(payload_h, signature)


    ###VERSÃO DO PROFESSOR.
    @staticmethod   ##static method pq __ NÃO UTILIZA NADA DE DENTRO DESSA CLASS 'wallet'...  ## TRANSPLANTEI ESSA FUNCTION para o arquivo/class de 'Utility'...
    def verify_transaction(transaction): 
        # if (transaction.sender == 'ourApp'): ##não é bom deixar isso no código, pois isso introduz uma FALHA DE SEGURANÇA...
        #     return True
            public_key = RSA.importKey(binascii.unhexlify(transaction.sender)) ##key extraída da transaction, inicialmente formato string, é convertida em BINARY DATA por meio de 'unxexlify' e 'importKey'...
            
            verifier = PKCS1_v1_5.new(public_key)
            payload_h = SHA256.new((str(transaction.amount) + str(transaction.recipient) + str(transaction.sender)).encode('utf8'))
            
            signature = binascii.unhexlify(transaction.signature)

            return verifier.verify(payload_h, signature)

            











# --> Professor explica que a pacakge de 




# 'Pycrypto'


# É 

# UMA PACKAGE __ SUPER ESTRANHA,



# e a pacakge que fazemos 'import from' 




# É UMA 

# PACKAGE QUE NÃO É CHAMADA DE 



# 'PyCrypto',

# E SIM SÓ 


# 'Crypto'..










# -----> O PROFESSOR N GOSTA MT DO NAMING DA PACKAGE DO 'pycrypto'...












# ---> from Crypto.PublicKey import RSA 











# --> 'RSA' --> é um ALGORITMO UTILIZADO NO GENERATE E TRABALHO 


# COM 

# PUBLIC E PRIVATE KEYS...














# --> NÓS TAMBÉM VAMOS PRECISAR DE UM __ NUMBER TOTALMENTE ALEATÓRIO (ou quase isso),


# POR ISSO 



# VAMOS IMPORTAR TAMBÉM A PACAKGE DE 




# 'Crypto.Random'...





# ex:











# from Crypto.PublicKey import RSA    ###'Crypto' --> é a package de 'Pycrypto'...
#                         ##### 'RSA' -> é um ALGORITMO USADO PARA O GENERATE E TRABALHO COM PUBLIC E PRIVATE KEYS...



# import Crypto.Random   ###gera um número realmente aleatório, supostamente....


# import binascii










# class Wallet:
#     def __init__(self):




#     def generate_keys(self):
        


# --------------------------------------------












# ISSO FEITO, VOLTAREMOS ATÉ 'generate_keys'


# E
#  ENTÃO 


#  ESCREVEREMOS 


#  A LÓGICA 




#  'RSA.generate' ----> dentro 





 



 

# PRIMEIRAMENTE VAMOS 

# PASSAR 
# OS 

# 'bits' 

# QUE 


# VAMOS QUERER GERAR...  ------> QUANTO MAIOR O NÚMERO, MAIOR A SEGURANÇA,


# MAS DEMORA MAIS TEMPO PARA ESSES 'bits' serem gerados...








# EX:











# from Crypto.PublicKey import RSA    ###'Crypto' --> é a package de 'Pycrypto'...
#                         ##### 'RSA' -> é um ALGORITMO USADO PARA O GENERATE E TRABALHO COM PUBLIC E PRIVATE KEYS...



# import Crypto.Random   ###gera um número realmente aleatório, supostamente....


# import binascii










# class Wallet:
#     def __init__(self):




#     def generate_keys(self):
#         RSA.generate(1024) ###quanto maior o número, maior a quantidade de bits e mais segura a key, mas mais tempo demora...
























#     --------> COMO SEGUNDO PARÂMETRO DE 

#     '.generate()',



#     PRECISAMOS __ de uma __ RANDOM FUNCTION.... ----> essa function 




#     VAMOS PEGAR LÁ DE 'Crypto.Random',

#     pq

#     ela encaixa direitinho...












#     --> para conseguir uma RANDOM FUNCTION 



#     nesse slot aí,


#     o professor 

#     chama 





#     'Crypto.Random.new()' 





# ----> ISSO  É UM METHOD QUE NOS DÁ UMA FUNCTION DESSAS, FUNCTION 'random'... ->  









# MAS NÃO É SÓ ISSO... --> PARA CONSEGUIR FAZER ESSA FUNCTION FUNCIONAR,

# precisamso 



# chainar '.read()' 


# em 'new()'..  ------> O READ VAI ESSENCIALMENTE 'PEGAR ESSA RANDOM FUNCTION QUE É GENERATED' 


# E ENTÃO VAI 

# __ A PASSAR___ ao '.generate()'....



