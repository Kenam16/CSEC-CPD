n = int(input())
nmb = list(map(int, input().split()))
a = 0
z = n - 1
s = 0
d = 0
t = 0
while a<=z:
    if nmb[a]>nmb[z]:
        temp = nmb[a]
        a+=1
    else:
        temp = nmb[z]
        z-=1
    if t==0:
        s+=temp
    else:
        d+=temp
    t = 1-t
print(s, d)


