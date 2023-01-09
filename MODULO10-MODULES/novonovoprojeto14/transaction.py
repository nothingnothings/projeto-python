from collections import OrderedDict

from util.printable import Printable



__all__ = ['Transaction']


# inheritamos a class de 'Printable', que COMPARTILHA O REPR DELE a essa class aqui..
class Transaction(Printable):
    def __init__(self, amount, recipient, signature, sender):
        self.amount = amount
        self.recipient = recipient
        self.sender = sender
        self.signature = signature

    def to_ordered_dict(self):
        return OrderedDict([('amount', self.amount), ('recipient', self.recipient), ('sender', self.sender)])
