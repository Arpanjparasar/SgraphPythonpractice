def write(name,age,email,path):
    cur = open(path,'w')
    cur.write(name)
    cur.write('\n')
    cur.write(age)
    cur.write('\n')
    cur.write(email)
    cur.close()



name=input('Enter the name ')
age=input('Enter the age ')
email=input('Enter the email ')
print(name)
print(age)
print(email)
path=r'E:\Sgraph Python practice\detail8.txt'

write(name,age,email,path)