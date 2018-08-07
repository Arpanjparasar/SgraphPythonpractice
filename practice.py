a=int(input('Enter the first number'))
b=int(input('Enter the second Number'))
op=input('Enter the operation(+,-,/,*)')

def add():
    print(a+b)

def sub():
    print(a-b)

def mult():
    print(a*b)

def divi():
    print(a/b)


if (op == '+'):
   add()
elif(op == '-'):
    sub()

elif(op == '*'):
    mult()

elif(op == '/'):
    divi()
else:
    print('Please enter a valid operation')