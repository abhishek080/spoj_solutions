def moveto(x,a):
	xcount=0
	for q in xrange(x,len(a)):
		
		if a[q]==')':
			xcount+=1
#			print a[q]
#			print xcount
			if xcount==1:
				#print xcount
				return q
		elif a[q]=='(':
			xcount-=1
#			print a[q]
#			print xcount
			if xcount==1:
				#print xcount
				return q

def main():
	t=input()
	for i in range(t):
		a=raw_input()
		a=list(a)
#		print a
		for j in xrange(len(a)-1,-1,-1):
#			print a[j]
			if a[j]=='+':
				m=moveto(j,a)
#				print m
				if m!=None:
					a.insert(m-1, a.pop(j))
#					print a
			elif a[j]=='-':
				m=moveto(j,a)
#				print m
				if m!=None:
					a.insert(m-1, a.pop(j))
#					print a

			elif a[j]=='*':
#				print j
				m=moveto(j,a)

#				print m
				if m!=None:
					a.insert(m-1, a.pop(j))
#					print a
			elif a[j]=='/':
				m=moveto(j,a)
#				print m
				if m!=None:
					a.insert(m-1, a.pop(j))
#					print a
			elif a[j]=='^':	
				m=moveto(j,a)
#				print m
				if m!=None:
					a.insert(m-1, a.pop(j))
#					print a
		a= ''.join(a)
		a= a.replace("(", "")
		a= a.replace(")", "")
		print a

	return

if __name__=="__main__":
	main()