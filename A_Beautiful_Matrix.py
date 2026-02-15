matrix = []
raw1 = 0
col1 = 0
for i in range(5):
    row = list(map(int,input().split()))
    for j in range (5):
        if row[j]==1:
            raw1 = i
            col1 = j
ans = abs(raw1-2)+abs(col1-2)
print(ans)