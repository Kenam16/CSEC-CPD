n, h = map(int, input().split())
k = list(map(int, input().split()))
count = 0
for b in k:
    if b>h:
        count+=2
    else:
        count+=1
print(count)