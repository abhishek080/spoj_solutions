import math
t=input()
for i in range(t):
    s=raw_input()
    str=s.split(' ')
    a=int(str[0])
    b=int(str[1])
    if(b==0):
        print 1
    else:
        a=a%10
        b=b%4
        if(b==0):
            b=4
        print pow(a,b)%10	