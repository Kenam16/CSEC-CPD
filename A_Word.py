k = input()
low = 0
up = 0
for i in range (len(k)):
    if k[i].islower():
        low+=1
    elif k[i].isupper():
        up+=1
if low>=up:
    print(k.lower())
elif low<up:
    print(k.upper())