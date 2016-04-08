for _ in xrange(input()):
	a, b, c = map(int, raw_input().split())
	n = (c*2)/(a+b)
	d = (b-a)/(n-5)
	m = a-2*d
	print n, '\n', " ".join(str(m+d*i) for i in range(n))