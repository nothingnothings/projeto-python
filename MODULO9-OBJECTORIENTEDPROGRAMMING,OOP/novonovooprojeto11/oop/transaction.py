from collections import OrderedDict

from printable import Printable


class Transaction(Printable): ###inheritamos a class de 'Printable', que COMPARTILHA O REPR DELE a essa class aqui..
    def __init__(self, amount, recipient, sender ):
        self.amount = amount
        self.recipient = recipient
        self.sender = sender
    
    def to_ordered_dict(self):
        return OrderedDict([('amount', self.amount), ('recipient', self.recipient), ('sender', self.sender)])

