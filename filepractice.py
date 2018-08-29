
name=input('Enter the name ')
m=open(r'E:\Sgraph Python practice\detailspractise.txt','r')
x=m.readlines()
print(x)

# Create an empty list.
lines = []

# Convert lines into string list.
for line in x:
    lines.append(line.rstrip())

print(lines)

if name in lines:
     print('Name present')

else:
    print('Name absent')



m.close()