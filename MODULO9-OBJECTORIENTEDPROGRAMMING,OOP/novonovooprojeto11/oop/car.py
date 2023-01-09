

# class SportsCar:   # a sintaxe é assim, 'MultiPalavra' (exataemnte como no javascript)....
#     top_speed = 100 #attribute/propriedade
#     def drive():  #method
#         print('I am driving, but certainly not faster than {}'.format(top_speed))  ##ISSO NÃO FUNCIONA, PQ __ ESSE METHOD VAI PROCURAR POR UMA VARIABLE __ COM ESSE NOME __ NO LADO _ DE FORA DE SUA CLASS, e não dentro de sua class (aquele ATTRIBUTE 'top_speed' ali será IGNORADO)..


# a sintaxe é assim, 'MultiPalavra' (exataemnte como no javascript)....
# class SportsCar:
#     top_speed = 100  # attribute/propriedade

#     # 'self' --> É ARGUMENTO AUTOMATICAMENTE 'PASSED IN' pelo python, ele automaticamente passa esse valor a todos os seus methods...  -> e 'self' TE DÁ ACESSO _ A TODOS __OS METHODS_ E ATTRIBUTES _ DE SUA CLASS..
#     def drive(self):
#         # print('I am driving, but certainly not faster than {}'.format(top_speed)) # não acesse seu attribute da class assim...
#         # acesse ASSIM...
#         print('I am driving, but certainly not faster than {}'.format(self.top_speed))


# # Nova instanciacao/objeto dessa class.... --> podemos rodar METHODS nisso...
# new_sports_car = SportsCar()


class SportsCar:
    top_speed = 100  # attribute/propriedade  --> é um CLASS ATTRIBUTE, definido aqui, dessa forma... ('solta')...
    # warnings = []  # uma list É UM REFERENCE TYPE, EM PYTHON....


    ## __xxx__ ---> é a sintaxe 'DUNDER', de que tanto falam....
    ##esse method/function built-in TAMBÉM RECEBE O ARGUMENTO 'self'...
    def __init__(self, starting_top_speed=100):  ####ISSO É A CONSTRUCTOR FUNCTION DAS NOSSAS CLASSES, EM PYTHON... é assim sua escrita... --> se você não escrever essa constructor function, o default de 'EMPTY CONSTRUCTOR FUNCTION' será utilizado...
                        ####os parâmetros subsequentes são os parâmetros 'NORMAIS' passados lá nas nossas instanciações...
        self.top_speed = 200  ####É ASSIM QUE CRIAMOS 'INSTANCE ATTRIBUTES'
        self.normal_speed = starting_top_speed
        self.warnings = []  ##INSTANCE ATTRIBUTE (attribute LOCAL)...

    # 'self' --> É ARGUMENTO AUTOMATICAMENTE 'PASSED IN' pelo python, ele automaticamente passa esse valor a todos os seus methods...  -> e 'self' TE DÁ ACESSO _ A TODOS __OS METHODS_ E ATTRIBUTES _ DE SUA CLASS..
    def drive(self):
        # print('I am driving, but certainly not faster than {}'.format(top_speed)) # não acesse seu attribute da class assim...
        # acesse ASSIM...
        print('I am driving, but certainly not faster than {}'.format(self.top_speed))






a_new_model = SportsCar( 'VERY FUCKING FAST')


print(a_new_model.normal_speed)



old_sports_car = SportsCar()






# Nova instanciacao/objeto dessa class.... --> podemos rodar METHODS nisso...
new_sports_car = SportsCar()


new_sports_car.drive()


new_sports_car.warnings.append('A')  ### essa alteração repercutirá _ NA NOSSA CLASS, O QUE VAI REPERCUTIR EM TODOS OS OBJECTS INSTANCIADOS A PARTIR DELA... (referential type values, isso em 'CLASS ATTRIBUTES''')...


# isso, esses redefines de CLASS ATTRIBUTES, NÃO DEVERIAM SER PERMITIDOS (leva a código imprevisível)..
SportsCar.top_speed = 200


generic_car = SportsCar()


generic_car.drive()


print(generic_car.warnings)

print(old_sports_car.warnings)







new_car = SportsCar(3000)




new_car.warnings.append('VALUE A')



print(new_car.warnings)



print(old_sports_car.warnings)


print(generic_car.warnings)