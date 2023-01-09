

from vehicle import Vehicle


class Bus(Vehicle):  ###INHERITANCE (inheritamos 'Vehicle' nessa class)...
    def __init__(self, starting_top_speed=200):
        # self.top_speed = starting_top_speed ###inherittados através da class 'Vehicle'...
        # self.__warnings = []
        # attribute EXCLUSIVO DE 'bus', qeu vamos querer manter nele (vamos querer mergear o constructor de 'bus' e de 'vehicle', a base class, para que fiquemos com isso)....
       super().__init__(starting_top_speed) #o call de 'super().__init__()' FAZ COM QUE TODOS OS ATTRIBUTES/METHODS do CONSTRUCTOR ORIGINAL, definidos lá, SEJAM _ INCORPORADOS _ NESSE NOVO CONSTRUCTOR, DESSA 'CLASS FILHA'..   --> NO CASO, O QUE O CALL DE 'SUPER' Faz é CHAMAR '''A BASE CLASS''' em si... --> E O SUPER É A COISA UQE _ _NOS DÁ _ ACESSO  à 'BASE CLASS' em si... ----->  JÁ O CALL DE '__init()__ 'serve PARA CHAMAR __ O CONSTRUCTOR __ DA BASE CLASS, QUE É O QUE INTERESSA... 
       self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus(200)


bus1.add_group(['Max', 'Manuel', 'Victoria'])


# esse passengers não faz parte da 'REPRESENTATION' do special method '__repr__', por isso não será influenciado por ele...
print(bus1.passengers)








bus1.add_warning('Test') #vai funcionar PQ A CLASS 'BUS' INHERITOU A CLASS 'Vehicle'.... (que é a class com esse method)




bus1.drive() #vai funcionar PQ A CLASS 'BUS' INHERITOU A CLASS 'Vehicle'.... (que é a class com esse method)