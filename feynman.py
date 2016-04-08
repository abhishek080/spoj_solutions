def feynman(n):
	if (n==1):
		return 1
	else:
		return n*n + feynman(n-1)
def main():
	a=True
	while a:
		t=input()
		if t:
			print feynman(t)
		else:
			a=False

if __name__=="__main__":
	main()


