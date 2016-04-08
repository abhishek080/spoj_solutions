while 1:
	t=input()
	if t!=0:
		x=map(int,str(t))
		l=len(x)
		y=[0]*l
		if x[0]!=0:
			y[0]=1
		x.append(1)
		for i in xrange(1,l):
			if x[i]!=0:
				y[i]=y[i-1]
				#print y
				#print "one"

			if x[i-1]!=0:
				if ((10*x[i-1])+x[i])<=26:
					if i<2:
						y[i]+=y[i-1]#+y[i-1	]

					#elif x[i]==0:
						#y[i]+=y[i-1]+y[i-2]
					else:
						y[i]+=y[i-2]
					#print y
					#print "two"
			if x[i]==0:
				y[i]=y[i-1]
				#y[i-1]=1

			if x[i+1]==0:
				y[i]=y[i-1]




			

		print y[-1]

	else:
		break