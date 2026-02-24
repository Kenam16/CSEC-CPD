k = int(input())
home = []
away = []

for i in range(k):
    h, a = map(int, input().split())
    home += [h]
    away += [a]

count = 0

for i in range(k):
    for j in range(k):
        if home[i] == away[j]:
            count = count + 1

print(count)