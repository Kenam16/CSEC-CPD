k = int(input())
count = 0
frs = input()
for i in range (k-1):
    if frs[i] == frs[i+1]:
        count+=1
print(count)
