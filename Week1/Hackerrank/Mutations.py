s = input()
p = input().split(' ')
num = p[0]
buk = p[1]

ans = list(s)
ans[int(num)] = buk
s = ''.join(ans)
print(s)