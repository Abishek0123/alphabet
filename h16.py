m,c=map(int,input().split())
ar=[[abs(i1-c),i1]for i1 in [int(x1) for x1 in input().split()]]
ar.sort()
ar=ar[1:]
ar=[i1[1] for i1 in ar[:3]]
print(*ar)
