t=input()
for _ in range(t):
	raw_input()
	x=input()
	s=[]
	count=0
	for i in range(x):
		s.append(input())

	for i in range(x-1):
		for j in xrange(i+1,x):
			if s[i]>s[j]:
				count+=1

	print count