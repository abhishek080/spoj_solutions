dct={1:1,2:2,3:6,4:24,5:120}

def fac(x):
	if x in dct.keys():
		return dct[x]
	else:
		fact=x*fac(x-1)
		dct[x]=fact
		return fact
for _ in range(input()):
	print fac(input())