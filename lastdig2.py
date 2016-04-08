#import math
for _ in range(input()):
	a,b=map(int,raw_input().split())
	#print a
	#print b
	if b==0:
		print 1
	else:
		c=b%4
		if c==0:
			c=4
		print (a**c)%10

