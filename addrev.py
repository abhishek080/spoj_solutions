def palindrome(num):
    return int(str(num)[::-1])

def main():
	t=input()
	for i in range(t):
		m,n=map(int,raw_input().split())
		m=palindrome(m)
		n=palindrome(n)
		add=m+n
		add=palindrome(add)
		print add

if __name__=="__main__":
	main()