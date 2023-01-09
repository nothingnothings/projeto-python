

# from vehicle import Vehicle


# import vehicle


from vehicle import Vehicle




class SportsCar(Vehicle):    ####### ESSA É A SINTAXE DE 'INHERITANCE' (vamos herdar a class de 'Vehicle', que é nossa BASE CLASS)..
        
    def brag(self):
        print('Look at how cool my car is.' )





car1 = SportsCar(1000)


print(car1)


print(car1.__dict__)


new_dict = car1.__dict__


new_dict.update({'newkey': 'value'})


print(new_dict)


print(car1.__dict__, 'OLD DICT')

print(car1)


print(car1)

print(car1.get_warnings(), 'WARNINGS') #get_warnings é DERIVADO LÁ DA BASE CLASS de 'vehicle'...


car1.add_warning('A WARNING TEXT') #add_warning TAMBÉM É DERIVADO LÁ DA INHERITED CLASS de 'vehicle'...
