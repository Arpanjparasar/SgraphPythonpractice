class passenger:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact

    def first(self):
        print('Name is :', self.name)
        print('Contact is :', self.contact)


    def second(passenger):
        pass

name=input('Enter the name')
contact=input('Enter the contact no')
obj = passenger(name,contact)
obj.first()