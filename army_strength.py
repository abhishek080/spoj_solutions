t=input()
for _ in range(t):
	x=raw_input()
	ng,nm=map(int,raw_input().split())
	g=map(int,raw_input().split())
	#g.sort(reverse=True)
	m=map(int,raw_input().split())
	#m.sort(reverse=True)


	if max(g)>=max(m):
		print "Godzilla"
	else:
		print "MechaGodzilla"