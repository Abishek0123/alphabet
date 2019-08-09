c,g = map(int,input().split())
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))
e =1
for i in l3:
    if i not in l2:
        print('NO')
        e = 0
        break
if(e):
    print('YES')
