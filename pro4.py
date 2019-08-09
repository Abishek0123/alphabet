a,b=map(str,input().split())
s=0
if len(a)>len(b):
  a,b=b,a
i=0
while i<len(a):
  s+=(ord(b[i])-ord(a[i]))
  i+=1
for i in range(i,len(b)):
  s+=ord(b[i])-ord('c')+1
print(s)
