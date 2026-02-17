k = int(input())
count = 1
r = input()
for i in range(k-1):
    p = input()
    if r != p:
        count+=1
    r = p 
print(count) 
