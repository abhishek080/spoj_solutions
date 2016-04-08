while 1:
	t=input()
	if t==-1:
		break
	else:
		y=0
		if t==1:
			y=1
		else:
			x=1
			i=1
			while x<t:
				i+=1
				x+=6*(i-1)
				if x==t:
					y=1

			if x>t:
				y=0
		if y==1:
			print "Y"
		else:
			print "N"