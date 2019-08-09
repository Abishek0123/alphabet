p,o=map(int,input().split())
a=[]
c1=[]
for i in range(p):
    li=[int(a) for ar in input().split()]
    a.append(li)
    if 0 in li:
        m=li.index(0)
        c1.append(m)
for i in range(len(a)):
    if 0 in a[i]:
        for j in range(o):
            a[i][j]=0
for i in c1:
    for j in range(p):
        a[j][i]=0
for i in a:
    print(*i)
