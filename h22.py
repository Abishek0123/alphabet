u=int(input())
ls=list(map(int,input().split()))
r=1
le=[]
for i in ls:
  r=r*i
for i in ls:
  le.append(r//i)
print(*le)
