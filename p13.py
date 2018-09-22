v,t=input().split()
v=int(v)
t=int(t)
s=list(input().split())
thirstydistance=v*t
for i in s:
    if thirstydistance<=int(i):
        print(i)
        break