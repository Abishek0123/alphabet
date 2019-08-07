n=int(input(""))
ar=list(map(int,input().split()))
length=len(ar)
large=max(ar)
x,y=0,0
for i in range(0,length-1):
 for j in range(i+1,length):
  if abs(ar[i]+ar[j])< large:
   x,y=ar[i],ar[j]
   large=abs(x+y)
print(x, y)
