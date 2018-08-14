import time
import threading
import random


class details:
    def inputs(self):
        name=[]
        for i in range(5):
            time.sleep(0.2)
            a=input('Enter the names :')
            name.append(a)

        print(name)
        return name

    def email(self,b):
        email=[]
        for i in range(len(b)):
            time.sleep(0.2)
            email.append(b[i]+ str(random.randint(50, 300))+'@mail.com')


        print(email)
        return email

    def enter(self,email,name):
        data=open(r'E:\Sgraph Python practice\detailspractise6.txt','a')
        k = str(name)
        s = str(email)
        data.write(k)
        data.write(s)



obj= details()
t=time.time()
b=obj.inputs()
c=obj.email(b)
t1=threading.Thread(target=obj.inputs, args=(b,))
t2=threading.Thread(target=obj.email, args=(c,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Done in ', time.time()-t)