'''Write a program that generates and prints 50 random integers, each between 3 and 6.'''
import random

for i in range(50):
    i=random.randint(3, 6)
    print(i)

print('\n')

#Write a program that generates a random number, x, between 1 and 50, a random number
#y between 2 and 5, and computes x y .

x=random.randint(1, 50)
y=random.randint(2, 5)
print(x)
print(y)
z=x+y
print(z)