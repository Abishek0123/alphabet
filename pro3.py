c,d=input().split()
f=abs(len(d)-len(c))
for i in range(len(c)):
    if(len(d)==1 and d[i] in c):
        break
    if (c[i]!=d[i]):
        f=f+1
print(f)
