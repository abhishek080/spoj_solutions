conv = {0:0}

def exch(num):
    if num in conv:
        return conv[num]
    else:
        conv[num] = max(num, exch(num/4)+exch(num/3)+exch(num/2))
        return conv[num]
while True:
    try:
        print exch(input())
    except:
        break