from math import sqrt
n = int(input())
s = input().split(' ')
a = [int(i) for i in s]
mx = a[0]
for i in a:
    mx = max(i, mx)
a = sorted(a)
for i in range(n-1, -1, -1):
    if mx > a[i]:
        print(a[i])
        exit()
print(mx)
