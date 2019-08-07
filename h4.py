try:
	a=int(input())
	ar=list(map(int,input().split()))
	for it in ar:
		if ar.count(it)==1:
			print(it)
except ValueError:
	print("invalid")
