def check_palin(b):
	if map(str,b)==map(str,b)[::-1]:
		return True

	else:
		return False


t=input()
for i in range(t):
	x=input()
	a=map(int,str(x))
	l=len(a)
	if (x+1)%10==0:
		print x+2

	elif check_palin(a):
		a[l/2]+=1
		print int(''.join(map(str, a)))

	else:
		j=l-1
		while j>=(l/2):
			if a[j]==a[l-j-1]:
				j-=1
				#continue
			else:
				if a[l-j-1]<a[j]:
					a[j]=a[l-j-1]
				else:
					a[l-j-1]=a[j]
				j-=1

		print "here"
		print a
		if check_palin(a):
			print int(''.join(map(str, a)))
