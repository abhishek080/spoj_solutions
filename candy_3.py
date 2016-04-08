#def main():
t=input()
for i in range(t):
	x=raw_input()
	a=input()
	#b=[]
	l=0
	for j in range(a):
		#b.append(input())
		l+=input()
	#print b
	if l%a==0:
		print "YES"
	else:
		print "NO"
