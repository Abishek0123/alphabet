v,z=map(str,input().split())
y=0
if len(v)>len(z):
  v,z=z,v
i=0
while i<len(v):
  y+=(ord(z[i])-ord(v[i]))
  i+=1
for i in range(i,len(z)):
  y+=ord(z[i])-ord('a')+1
print(y)
