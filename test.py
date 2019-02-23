import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

if a < 0 or b <= 0:
    print('error')
else:
    x = math.sqrt(a*b) / (math.pow (math.e, (a) ) * b ) + (a * math.pow (math.e, (2*a/b)))
    print(x)
