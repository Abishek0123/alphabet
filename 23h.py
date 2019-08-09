v,z=map(eval,input().split())
aut=[]
for k in range(v):
  aut.append(list(map(eval,input().split())))
n=[]
m=[]
tmp_out=[]
t=[]
s=0
j=0
m.append(aut[k][j])
n.append([k,j])
while [v-1,z-1] not in n:
  k=0
  for x in n:
    if x[0]+1<v and x[1]+1<z:
      tmp_out.append(aut[x[0]+1][x[1]]+m[s])
      tmp_out.append(aut[x[0]][x[1]+1]+m[s])
      t.append([x[0]+1,x[1]])
      t.append([x[0],x[1]+1])
    elif x[0]+1<v:
      tmp_out.append(aut[x[0]+1][x[1]]+m[s])
      t.append([x[0]+1,x[1]])
    elif x[1]+1<z:
      tmp_out.append(aut[x[0]][x[1]+1]+m[s])
      t.append([x[0],x[1]+1])
    s+=1
  n=t
  t=[]
  out=tmp_out
  tmp_out=[]
print(max(out))
