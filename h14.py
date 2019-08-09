def toString(list):
    return ''.join(list)
def per(b,k,v):
    if k==v:
        print(toString(b))
    else:
        for i in range(k,v+1):
            b[k],b[i]=b[i],b[k]
            per(b,k+1,v)
            b[k],b[i]=b[i],b[k]
str=input()
n=len(str)
nm=list(str)
per(nm,0,n-1)
