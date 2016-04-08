def main():
	while 1:
		t=input()
		if t==0:
			break

		else:
			a=raw_input()
			l=len(a)
			b=[]
			for i in range(t):
				#b.append(a[i])
				j=i
				while j<l:
					b.append(a[j])
					#print ''.join(b)
					j+=(2*t)-1-(2*i)
					if j<l:
						b.append(a[j])
					#	print ''.join(b)
					j+=1+(2*i)
		b="".join(b)
		print b
	return

if __name__=="__main__":
	main()
