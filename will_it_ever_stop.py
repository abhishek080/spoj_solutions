def check(n):
	x=n
	a=[]
	while n>1:
		if n%2==0:
			n=n/2
		else:
			n=(3*n)+3

		if n in a:
			return 1
		else:
			a.append(n)

	return 0


t=input()

if check(t)==0:
	print "TAK"
else:
	print "NIE"