class emp:
    def __init__(self,name,email):
        self.name=name
        self.email=email


    def display(self):
        print('Name is :',self.name)
        print('Email is :', self.email)

a=input('Enter the Name:')
b=input('Enter the Email')

obj=emp(a,b)
obj.display()