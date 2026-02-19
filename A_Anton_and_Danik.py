t = int(input())
ant = 0
dar = 0
r = list(input().upper())
for i in range (t):
    if r[i]=="A":
        ant+=1
    elif r[i]=="D":
        dar+=1
if ant>dar:
    print("Anton")
elif ant<dar:
    print("Danik")
else:
    print("Friendship")
    