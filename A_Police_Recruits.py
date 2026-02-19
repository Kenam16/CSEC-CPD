k = int(input())
s = map(int, input().split())
p = 0
r = 0
for i in s:
    if i==-1:
        if p>0:
            p-=1
        else:
            r+=1
    else:
        p+=i
print(r)