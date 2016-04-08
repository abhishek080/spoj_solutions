t=input()
for i in range(t):
	raw_input()
	a=raw_input().split()
	y='machula'
	#print a
	for j in range(len(a)):
	#	print a[j]
		if y in a[j]:
			pos=j
		if (y not in a[j]) and a[j]!='+' and a[j]!='=':
	#		print a[j]
			a[j]=int(a[j])
		

	#print a
	x=[]

	for j in range(len(a)):
		if type(a[j]) is int:
			x.append(a[j])

	#print x
	z=0
	if pos<4:
		z=x[1]-x[0]
	else:
		z=x[1]+x[0]
	if z<0:
		z=z*-1
	for j in range(len(a)):
		if  (type(a[j]) is str) and (y in a[j]):
			a[j]=z

	for j in range(len(a)):
		if type(a[j]) is int:
			a[j]=str(a[j])

	#print a
	for j in a:
		print j," ",

	print "\n"