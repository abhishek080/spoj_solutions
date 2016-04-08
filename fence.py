from math import pi
#Note: if you length is in feet, the area is in sq. ft.

c = 1 / (2*pi)
while True:
    L = int(raw_input())
    if L == 0: break
    print '%.2f' % (L*L*c)