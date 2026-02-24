k = int(input())
r = []
t = []
for i in range(k):
    h, a = map(int, input().split())
    r += [h]
    t += [a]
count = 0
for i in range(k):
    for j in range(k):
        if r[i] == t[j]:
            count = count + 1
print(count)
