t = int(input())
solved_num = 0
for i in range (t):
    x , y , z = map(int, input().split())
    if x+y+z>=2:
        solved_num+=1
print(solved_num)