import math
def main():
	t=input()
	count=0
	#count+=t
	for i in xrange(1,int(t**0.5)+1):
		#print i
		count+=(t/i)-i+1

	print count
	return

if __name__=="__main__":
	main()
