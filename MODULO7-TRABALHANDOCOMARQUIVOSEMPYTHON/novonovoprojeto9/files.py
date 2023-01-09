

# f = open('demo.txt', mode='w')  #MODO DE WRITE --> vamos querer ESCREVER ALGO NESSE ARQUIVO... ### O DEFINE DO 'MODE' que você quer é _EXTREMAMENTE IMPORTANTE --> se você naõ escreve o 'mode', O PYTHON AUTOMATICAMENTE ASSUME QUE VOCÊ VAI QUERER O MODO DE 'read'...



# f.write('Hello from Python!')



# f.close() #absolutamente INDISPENSÁVEL PARA CONSEGUIRMOS FAZER 'WRITE' de coisas no python... (você tem que FECHAR ESSA EXECUTION DE 'write' ANTES DE TENTAR EXECUTAR QUALQUER OUTRA LINHA DE CÓDIGO POSTERIOR, como esse 'input', no nosso exemplo...)








h = open('demo.txt', mode='a') 


h.write('Add this content in multi-lines!\n')    #meio de fazer WRITE DE SUA STRING EM MULTILINES, NOS SEUS ARQUIVOS...

h.close()


# user_input3 = input('Enter something... we will bother write script execution:   ')









p = open('demo.txt', mode='r')



# file_content = p.read() #retorna o conteúdo todo dessa text file EM UMA LONGA STRING, tudo junto (e com '\n' sinalizando os LINE BREAKS)...

file_content = p.readlines() #retorna o conteúdo todo dessa text file EM UMA __ LIST__ DE STRINGS, 1 STRING/ELEMENTO NA LIST _ PARA __ CADA __ LINHA...c

p.close()



print(file_content)

for line in file_content:
    altered_line = line[:-1]  #vai nos retornar cada LINE sem o caracter '\n' ao final, por meio desse RANGE SELECTOR com '-1'... (OBS::: o '\n' CONTA COMO 1 ÚNICO CARACTER, APESAR DE SER 2... )
    print(altered_line, 'LINE')



##############################################




# g = open('demo.txt', mode='w') ### se você definir o modo como 'write' e NAÕ ESCREVER NADA (tentar rodar o 'g.read()', que vai falhar, ams que não VAI ESCREVER COISA ALGUMA), O CONTEÚDO DE SEU FILE AINDA SERÁ OVERWRITTADO por esse statement de 'open('demo.txt', mode='w')'



# g_content_read = g.read() #necessário pARA CONSEGUIRMOS ACESSAR O VALOR DESSE ARQUIVO 'demo.txt'...



# print(g_content_read, 'LINE')

# g.close()


# user_input = input('Enter something... we will bother write script execution:   ')


#####################################################










# g = open('demo.txt', mode='a') #MODO DE APPEND --> vamos querer FAZER APPEND DE ALGO AO FINAL DE UM ARQUIVO JÁ EXISTENTE, SEM DELETAR A DATA ANTIGA CONTIDA NELE...
#                                 #NA SUA FORMA MAIS BÁSICA, ESSE CÓDIGO DE APPEND FARÁ COM QUE A STRING SEJA COLOCADA EM __ APENAS 1 ÚNICA LINHA DO SEU ARQUIVO DE TEXTO (coisa bem feia)...
                        

# g_content_read = g.write('CONTENT ADDED TO THE END OF YOUR FILE') #necessário pARA CONSEGUIRMOS ACESSAR O VALOR DESSE ARQUIVO 'demo.txt'...



# print(g_content_read, 'LINE')

# g.close()


# user_input2 = input('Enter something... we will bother write script execution:   ')



























# h = open('demo.txt', mode='r') #MODO DE READ --> vamos querer LER ESSE ARQUIVO... ### O DEFINE DO 'MODE' que você quer é _EXTREMAMENTE IMPORTANTE --> se você naõ escreve o 'mode', O PYTHON AUTOMATICAMENTE ASSUME QUE VOCÊ VAI QUERER O MODO DE 'read'...



# h_content_read = h.read() #necessário pARA CONSEGUIRMOS ACESSAR O VALOR DESSE ARQUIVO 'demo.txt'...



# print(h_content_read, 'LINE')

# h.close()


# user_input3 = input('Enter something... we will bother write script execution:   ')








#OPEN RETORTNA UM OBJETO 'file', com o qual podemos interagir... (e devemos interagir, para lidar com essa file)...

# 'r' read access ONLY
 

# 'w' WRITE ACCESS ONLY




# 'r+' READ E WRITE ACCESS 




# 'X' ---> ESSE _ TAMBÉM É UM 'WRITE ACCESS', MAS _ ELE _ SÓ VAI FAZER O WRITE _ SE CONSTATAR QUE ESSE FILE AINDA NAÕ EXISTE...




# 'A' (a) -->  É USADO SE VOCê QUER __ ABRIR UMA FILE JÁ EXISTENTE __ ,



# MAS __ NÃO VAI QUERER _ OVERWRITTAR __ A FILE INTEIRA,

# E SIMN 


# SÓ 

# FAZER 


# APPEND 




# de seu write __ AO FINAL DESSE ARQUIVo....









# 'B' --> ISSO __ É USADO __ QUANDO VOCÊ 




# ''NÃO QUER ESCREVER TEXT AOS ARQUIVOS'' (que é o procedimento PADRÃO),





# E SIM 



# QUANDO VOCê QUER __ ARMAZENAR 'BINARY DATA' (data não legível por humanos)...