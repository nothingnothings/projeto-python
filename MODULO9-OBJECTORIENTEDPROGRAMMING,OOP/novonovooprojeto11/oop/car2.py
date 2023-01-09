

class SportsCar:

    top_speed = 100

    def __init__(self, starting_top_speed=100):
        self.top_speed = 200
        self.normal_speed = starting_top_speed
        self.warnings = []

    def __repr__(self): ##TODOS OS SPECIAL METHODS de objects (dunder functions) EXIGEM QUE VOCê PASSE 'self' COMO PRIMEIRO PARÂMETRO...
        #esse method SEMPRE EXIGE O RETURN DE ALGUM VALOR (Que vai basiacmente ser o valor RETORNADO QUANDO VOCê OUTPUTTAR ESSA CLASS...)
        print('Printing...')
        return 'Top Speed: {}, warnings: {}'.format(self.normal_speed, len(self.warnings))
      

    def drive(self):
        print('I am driving, but certainly not faster than {}'.format(self.top_speed))










car1 = SportsCar(1000) 



car10 = SportsCar(2000)



print(car1) ## nos dá um output insatisfatório de nossa instance, pq vai dar apenas a LOCALIZAÇAÕ DE NOSSA INSTANCE NA MEMÓRIA DE NOSSO APP --> ex:  <__main__.SportsCar object at 0x000001BAA76EE9E0>








print(car1.__dict__)  ###vai printar toda nossa class como KEYS E VALUES... (IGNORADOS OS METHODS DA CLASS, NESSE OUTPUT --> NAÕ APARECEM....)





new_dict = car1.__dict__





new_dict.update({'newkey': 'value'})





print(new_dict)




print(car1.__dict__, 'OLD DICT')

print(car1)