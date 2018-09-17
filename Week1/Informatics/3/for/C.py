import functools
import math
 
a = int(input())
b = int(input())
 
for x in range(a, b + 1):
    d = int(math.sqrt(x))
    if d * d == x:
        print(x)
 
 
#c = str(a)[::-1]
 