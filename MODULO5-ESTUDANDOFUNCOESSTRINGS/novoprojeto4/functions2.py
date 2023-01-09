# * tells Python to accept an unlimited amount of unnamed arguments and pass them into the function as a tuple
# ** tells Python to accept and unlimited amount of named arguments and pass them into the function as a dictionary
def unlimited_arguments(*args, **keyword_args):
    # print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)

    for argument2 in args:
        print(argument2)


unlimited_arguments(1,2,3,4, name='Max', age=29) 



unlimited_arguments(*[1,2,3,4])  #o asterisco vai fazer com que essa list seja SPREAD/retirados os números de dentro da list e INSERIDOS COMO ARGUMENTOS NAQUELE '*args'....








a = [1, 2 , 3]




print('Some text: {} {} {}'.format(*a))  #o '*' FUNCIONA __ DE FORMA MT SIMILAR_ AO 'SPREAD/REST OPERATOR' lá do javascript....------> ESSA SINTAXE FARÁ COM QUE SEUS ARGUMENTOS NAQUELA LIST __ SEJAM __ ESPALHADOS__ nesses slots dessa string...


