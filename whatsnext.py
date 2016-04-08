def main():
	a=True
	while a:
		m,n,o=map(int,raw_input().split())
		if m==0 and n==0 and o==0:
			a=False
			break
		x=n-m
		y=n/m
		if o==n+x:
			print "AP ",
			print o+x
		elif o==n*y:
			print "GP",
			print o*y
	return

if __name__=="__main__":
	main()