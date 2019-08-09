n=int(input())
k=[]
for x in range(0,n):
 la=input()
 k.append(la)
new=[]
for x in zip(*k):
 if(x.count(x[0])==len(x)):
  new.append(x[0])
 else:
  break
print(''.join(new))
