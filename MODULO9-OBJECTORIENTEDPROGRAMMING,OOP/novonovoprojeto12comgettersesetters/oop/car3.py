

class SportsCar:

    top_speed = 100

    def __init__(self, starting_top_speed=100):
        self.top_speed = 200
        self.normal_speed = starting_top_speed
        # self.warnings = []   ###PUBLIC ATTRIBUTE... é assim que são escritos/adicionados
        self.__warnings = [] ###PRIVATE ATTRIBUTE.... necessário o '__', é assim que são escritos/adicionados... --> só pode ser acessado do lado de DEntro da sua class... (por meio de methods)..

    def __repr__(self):

        print('Printing...')
        return 'Top Speed: {}, warnings: {}'.format(self.normal_speed, len(self.__warnings))

    def drive(self):
        print('I am driving, but certainly not faster than {}'.format(self.top_speed))

    def add_warning(self, warning_text): ###exemplo de PUBLIC E PRIVATE ATTRIBUTES/methods....
        if (len(warning_text) > 0):
            self.__warnings.append(warning_text)

    def get_warnings(self):  #só assim você conseguirá printar os WARNINGS, se você usar uma function call como 'print(car1.get_warnings())'....
        return self.__warnings



car1 = SportsCar(1000)


print(car1)


print(car1.__dict__)


new_dict = car1.__dict__


new_dict.update({'newkey': 'value'})


print(new_dict)


print(car1.__dict__, 'OLD DICT')

print(car1) ###mostra como funciona o 'REPR' lá no 




# print(car1.__warnings)


print(car1)

print(car1.get_warnings(), 'WARNINGS') #vai nos printar os '__warnings' dentro desse object...

# car1.warnings.append('A WARNING TEXT')



car1.add_warning('A WARNING TEXT')