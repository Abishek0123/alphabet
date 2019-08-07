n=int(input())
ls=input().split()
for it in range(0,len(ls)):
    if(it%2==0):
        if(int(ls[it])%2==1):
            print(ls[it],end=' ')
    else:
        if(int(ls[it])%2==0):
            print(ls[it],end=' ')
