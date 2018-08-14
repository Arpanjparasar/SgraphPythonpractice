import time
import threading
import random


class details:
    def inputs(self):
        a1 = input('Enter first name :')
        a2 = input('Enter second name :')
        a3 = input('Enter third name :')
        a4 = input('Enter fourth name :')
        a5 = input('Enter fifth name :')
        foo=[a1,a2,a3,a4,a5]
        print(foo)

        foo1={}
        for i in foo:
            r = str(random.randint(50, 300))
            foo1[i]=i+r+'@mail.com'

        print(foo1)

obj= details()
obj.inputs()
