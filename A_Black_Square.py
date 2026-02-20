a, b, c, d = map(int,input().split())
k = input()
count = 0
for x in k:
    if x=="1":
        count+=a
    elif x=="2":
        count+=b
    elif x=="3":
        count+=c
    elif x=="4":
        count+=d
print(count)
