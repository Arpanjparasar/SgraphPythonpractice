def check(f):
    def validate(a):
        if(a == 0):
            print('Cannot divide by zero')
        elif(a==str(a)):
            print('List contains a string')
        else:
            f(a)
    return validate

@check
def divide(x):
    print(1/x)

foo=[1,2,3,4,5,0,'jgtj']

for i in foo:
    divide(i)
