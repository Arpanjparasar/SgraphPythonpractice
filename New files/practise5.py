import random
class passenger:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
        self.pnr=random.randint(5000,20000)
class first(passenger):
    def __init__(self,name,contact):
        super().__init__(name,contact)

    def display(self):
        print('Name is :', self.name)
        print('Contact is :', self.contact)
        print('PNR number is :', self.pnr)
        print('Meals are free')

class second(passenger):
    def __init__(self,name,contact):
        super().__init__(name,contact)

    def display(self):
        print('Name is :', self.name)
        print('Contact is :', self.contact)
        print('PNR number is :', self.pnr)
        print('Meals are not free')

def callObj(obj):
    obj.display()

name=input('Enter the name')
contact=input('Enter the contact no')
bclass=input('Enter the class(first/second)')
fc=first(name,contact)
sc=first(name,contact)
if(bclass=='first'):
    callObj(fc)
elif(bclass=='second'):
    callObj(sc)
else:
    print('Enter valid class')