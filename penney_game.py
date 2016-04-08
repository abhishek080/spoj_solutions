for _ in range(input()):
	s = {"TTT":0,"TTH":0,"THT":0,"THH":0,"HTT":0,"HTH":0,"HHT":0,"HHH":0}
	t = input()
	a = raw_input()
	for i in range(38):
		s[a[i:i+3]] += 1
	print t,
	tosses=["TTT","TTH","THT","THH","HTT","HTH","HHT","HHH"]
	for j in tosses:
		#print j,
		print s[j],
		#print str(s)
	print ""
