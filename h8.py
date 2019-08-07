n=int(input())
ls=input().split()
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        for a in range(j+1,len(ls)):
            if(int(ls[i])+int(ls[j])==int(ls[a])):
                print(ls[i],ls[j],ls[a])
