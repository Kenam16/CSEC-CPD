k = input()
t = input()
p = 0
for ch in t:
    if p < len(k):
        if ch == k[p]:
            p += 1
print(p + 1)