n=list(map(str,input()))
s=c=0
for i in range(0,len(n)-1):
  a=n[i]
  if int(a)!=0:
   for j in range(i+1,i+2):
    a=a+n[j]
    if int(a)<27 and int(a)>0: s=s+1
    elif int(a)==0: s=s-1
    else: break
if s!=1: c=s%2
print(s+c+1)
