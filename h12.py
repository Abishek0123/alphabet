a,b=input().split()
n1=int(a)
n2=int(b)
l1=list(map(int,input().split()))
l2=sorted(l1)
e=l2[::-1]
print(e[n2-1])
