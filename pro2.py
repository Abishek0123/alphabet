from itertools import combinations
y,c=list(input().split())
k=[]
c=int(c)
length=combinations(y,len(y)-c)
for i in length:
  k.append("".join(i))
print(min(k))
