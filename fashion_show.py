t=input()
for i in range(t):
	n=input()
	a=sorted(map(int,raw_input().split()))
	b=sorted(map(int,raw_input().split()))
	count=0
	for j in range(n):
		count+=a[j]*b[j]
	print count
