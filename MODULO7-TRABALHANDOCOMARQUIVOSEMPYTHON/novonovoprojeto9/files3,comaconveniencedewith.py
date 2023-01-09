# f = open('demo.txt', mode='r')
with open('demo.txt', mode='r') as f:  ### CONVENIENCE WITH BLOCK KEYWORD... --> você pode usar isso para EVITAR TER DE FICAR CHAMANDO 'f.close()' toda hora, com suas operações de FILE ACCESS...
### file está armazenado nessa varia´vel de 'f'...
    line = f.readline()


    while line:
        print(line)
        line = f.readline()
    
    # f.close()


print('Done, file is already closed... the with block closed it')
user_input = input('Testing..., please input something:  ')
print(user_input)




### O 'with' BLOCK VAI _ AUTOMATICAMENTE DAR 'close' nesse file armazenado na variável de 'f' quando ESTIVER ACABADO COM ESSAS LINHAS DE CÓDIGO...







with open('demo3.txt', mode='w') as g:  ### CONVENIENCE WITH BLOCK KEYWORD... --> você pode usar isso para EVITAR TER DE FICAR CHAMANDO 'f.close()' toda hora, com suas operações de FILE ACCESS...
    g.write('Testing if this closes...')
    
    
    
print('Done, file is already closed... the with block closed it')


user_input = input('Testing: ')

print(user_input)


