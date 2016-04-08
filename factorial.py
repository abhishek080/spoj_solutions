import math
def main():
	t=input()
	for i in range(t):
		n=input()
		#m=math.factorial(n)
		count=0
		j=1
		a=True
		while a:
			b=n/(5**j)
			#print b
			if b:
				count+=b
			else:
				a=False
			j+=1
		print count

	return

if __name__=="__main__":
	main()
