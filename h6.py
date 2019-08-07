c=input()
flag=0
b=[int(l) for l in input().split()]
for i in b:
    if(b.count(i)!=1):
        flag=1
        break
if(flag==1):
    print(i)
else:
    print("unique")
