import functools
import math
cnt = 0
sum = 0
x = int(input())
i = 1
bl = False
while i < x + 1:
    if i == x:
        print("YES")
        bl = True
    i *= 2
if bl==False:
    print("NO")
#c = str(a)[::-1]
 