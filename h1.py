try:
	num=int(input())
	array=list(map(int,input().split()))
	ef=[]
	for i in array:
		if array.count(i)>1:
			if i not in ef:
				ef.append(i)
	print(*ef)
	if len(ef)==0:
		print("unique")
except ValueError:
	print("invalid")
