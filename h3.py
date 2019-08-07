num=int(input())
ls=input().split(" ")
ls=[int(num) for num in ls]
final=[]
for x in range(0,num):
  if(x==ls[x]):
    final.append(ls[x])
if not(len(final)==0):
  final=sorted(final)
  for i in range(0,len(final)):
    print(final[i],end=' ')
else:
  print("-1")
