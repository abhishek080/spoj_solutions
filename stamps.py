t=input()
for i in range(t):
	print "Scenario #"+str(i+1)+":"
	a,b=map(int,raw_input().split())
	c=map(int,raw_input().split())
	c.sort()
	x=0
	count=0
	l=len(c)
	#print "c ",c
	#print "l ",l
	#print c
	while x<a and l>0:
		if len(c)!=0:
			d=c[l-1]
	#		print "d ",d
			x+=d
	#		print "x ",x

			#c.remove(d)
	#		print c
			l-=1
	#		print "l ",l

			count+=1
		else:
			break

	if x>=a:
		print count
	else:
		print "impossible"
