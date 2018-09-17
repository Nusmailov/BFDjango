from math import sqrt
 
a = int(input())
b = int(input())
c = str(a)[::-1]
d = str(a)
if a/1000 > 0 and c == d and b == 1:
    print("NO")
else: print("YES")