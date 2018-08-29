class human:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location
        print('Hi I am called')
    def display(self):
        print('name is',self.name)
        print('age is', self.age)
        print('location is', self.location)

name=input("Enter the  name :")
age=input('Enter the age ')
loc=input('Enter the location ')
obj=human(name,age,loc)
obj.display()
