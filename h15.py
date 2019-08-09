n=int(input())
ar=list(map(int,input().split()))
e=0
f=[]
m=[]
for i in range(0,len(ar)):
    for j in range(i+1,len(ar)):
        if ar[i]<ar[j]:
            e=e+1
            break
    else:
        f.append(ar[i])        
print(*f)
print(max(ar))
