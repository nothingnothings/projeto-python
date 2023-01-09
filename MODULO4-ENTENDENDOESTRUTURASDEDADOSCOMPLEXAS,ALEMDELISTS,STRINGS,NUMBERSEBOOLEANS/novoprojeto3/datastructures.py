

simple_list = [1, 2, 3, 4]


del simple_list[2]


# simple_list.remove() ou isso

# ou isso: 'del()'...

# del(simple_list[2])

# ou isso (sintaxe popular):  del simple_list[0]

simple_list.extend([5, 6, 7])
    # [1, 2, 3, 4, 5, 6, 7]

print(simple_list)







d = {'name': 'Max'}.copy()  #COPY SEMPRE FAZ UMA 'SHALLOW COPY' desse dictionary ---> se você tiver armazenado uma COMPLEX DATA STRUCTURE AINDA DENTRO DESSES KEY-VALUE PAIRS (como um set, list, tuple ou dict) , ELE NÃO SERÁ COPIADO, E SIM __ SÓ _ _SEU 'POINTER' a essa data structure será copiado...







print(d.items()) #isso retorna uma LIST DE TODOS OS DICT ITEMS....
for key, value in d.items():
    print(key, value)




set = {'Max', 'Manu', 'Max'}



tuple = (1, 2, 3)

print(tuple.index(3))


















#del()   ou       del list_name     del(list_name[2])  del(dict_name['crap'])




# ^^^^ ESSA SINTAXE AÍ, DE 'del', FUNCIONA COM LISTS, E DICTIONARIES, MAS _ NÃO FUNCIONA COM TUPLES.... (pq tuples SÃO IMMUTABLE, ESSA É A RAZÃO) --> TAMBÉM NÃO FUNCIOAN COM SETS, PQ SETS NÃO SUPORTAM INDEXES...




# se quer remover um ELEMENTO DE UM SET, VOCê É OBRIGADO A USAR 'set.discard()'...


