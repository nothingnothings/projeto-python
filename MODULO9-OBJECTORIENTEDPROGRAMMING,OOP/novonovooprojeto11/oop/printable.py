class Printable:  ##típico use-case de INHERITANCE, para outputtar coisas de nosso código...
    

    def __repr__(self):
        return str(self.__dict__)


