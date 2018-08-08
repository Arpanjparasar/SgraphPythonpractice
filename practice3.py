foo=[1,2,3,2,2,1,1,3,55,55,77]
fo={}
for i in foo:
    fo[i]=foo.count(i)

print(fo)