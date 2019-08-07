num=int(input())
ls=list(map(int,input().split()))
ls.sort()
ls.reverse()
if ls[0]==0:
    print(0)
else:
    for i in ls:
        print(i,end='')
