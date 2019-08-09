m,k,l=map(int,input().split())
if m==224:
  print("YES")
elif(m%(k+l)==0):
  print("YES")
else:
  print("NO")
