l,b = map(int,input().split())
count = 0
while l<=b:
    count+=1
    l=l*3
    b=b*2
print(count)