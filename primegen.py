
def primes1(m,n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n-m+1)
    for i in xrange(m,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


def main():
	t=input()
	for i in range(t):
		a=map(int,raw_input().split())
		m=a[0]
		n=a[1]
		prime=[True]*(n-m+1)
		for num in range(m,n+1):
		   # prime numbers are greater than 1
		   if num > 1:
		       for i in range(2,int(num**0.5)+1):
		           if (num % i) == 0:
		    		   prime
		               break
		       else:
		           print(num)
#	b=[]
#	b=primes1(m,n)
#	for i in b:
#		print i

	

if __name__=="__main__":
	main()
