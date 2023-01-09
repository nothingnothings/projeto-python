










f = open('demo.txt', mode='r')




print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())


f.close()










g = open('demo.txt', mode='r')




line = g.readline()
number = 0

while line:
    print(line, number)
    number += 1
    line = g.readline()
else:
    number = 0
    print(number)


    
# ----> ISSO VAI REALMENTE 
# LER TODAS AS LINES __ ATÉ _ SE EXAURIREM.,...

# -----> COMO VOCÊ PODE VER, 

# o 

# 'readline()'


# AUTOMATICAMENTE FAZ 'step through lines',



# __ 1 POR VEZ,


# CADA VEZ QUE É EXECUTADO.. .. -> ISSO SIGNIIFCA QUE VOCê NÃO PRECISA 'DIZER A ELE PARA QUE VÁ ATÉ A OUTRA LINHA, PQ ELE FAZ ISSO AUTOMATICAMENTE...'