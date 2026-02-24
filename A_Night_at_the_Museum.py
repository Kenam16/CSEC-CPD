k = input()
t = "a"
count = 0
for x in k:
    c = abs(ord(x)-ord(t))
    count+=min(c,26-c)
    t = x
print(count)