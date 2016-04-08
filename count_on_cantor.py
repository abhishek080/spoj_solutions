t=input()
for _ in range(t):
	x=input()
	c=0
	y=0
	i=1
	while c<x:
		y=c
		c+=i
		i+=1
		#print "c ",c
		#print "y ",y
		#print "i ",i
	z=i
	#print "z ",z
	#print "c ",c
	#y-=z
	#print "y ",y
	i-=2
	#print "i ",i
	a=[]
	for j in xrange(1,z):
		a.append(j)
	q=0
	#print "a ",a
	while y<=x:
		if y==x:
			if (z-1)%2==0:
	#			print "hi"
				print "TERM",x,"IS",str(a[q-1])+"/"+str(z-a[q-1])
			else:
				print "TERM",x,"IS",str(z-a[q-1])+"/"+str(a[q-1])

		y+=1
		q+=1
	#	print "y ",y
	#	print "q ",q
