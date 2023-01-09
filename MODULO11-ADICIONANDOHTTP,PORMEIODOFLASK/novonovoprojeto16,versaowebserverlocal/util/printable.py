"""""Helper class used to print various things, such as our blockchain"""

__all__ = ['Printable']


class Printable:

    def __repr__(self):
        return str(self.__dict__)
