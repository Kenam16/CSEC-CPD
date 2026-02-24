n = int(input())
b = list(map(int, input().split()))
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    x = x - 1
    l = y - 1
    r = b[x] - y
    if x > 0:
        b[x - 1] = b[x - 1] + l
    if x < n - 1:
        b[x + 1] = b[x + 1] + r
    b[x] = 0
for i in range(n):
    print(b[i])