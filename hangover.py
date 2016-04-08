while True:
	c, l, n = float(raw_input()), 0, 2
	if c == 0: break
	while c > 0:
		c-= 1.0/n
		n+= 1
	print n-2, 'card(s)'