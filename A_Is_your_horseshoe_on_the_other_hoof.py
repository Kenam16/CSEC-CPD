a, b, c, d = map(int, input().split())
count = 0
if a == b or a == c or a == d:
    count += 1
if b == c or b == d:
    count += 1
if c == d:
    count += 1
print(count)