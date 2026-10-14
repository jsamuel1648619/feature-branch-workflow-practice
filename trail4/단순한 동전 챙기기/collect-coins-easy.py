def select(level,start):
    if len(nums)<3:
        return
    if level==3:
        result.append(move[:])
        return
    for i in range(start,len(nums)):
        move.append(nums[i])
        select(level+1,i+1)
        move.pop()


n = int(input())
arr = [list(input())for _ in range(n)]
nums = []
move = []
result = []
min_v = float('inf')
# 격자 안에 몇 번 동전이 있는지
for i in range(n):
    for j in range(n):
        if arr[i][j].isdigit():
            nums.append(int(arr[i][j]))
nums.sort()
select(0,0)
for i in range(n):
    for j in range(n):
        if arr[i][j]=='S':
            start = (i,j)
        elif arr[i][j]=='E':
            end = (i,j)
coin_pos = {}
for r in range(n):
    for c in range(n):
        if arr[r][c].isdigit():
            num = int(arr[r][c])
            coin_pos[num]=(r,c)

for x in result:
    coin = [start]
    for num in x:
        coin.append(coin_pos[num])
    coin.append(end)
    v = 0
    for i in range(4):
        v += abs(coin[i+1][0]-coin[i][0])
        v += abs(coin[i+1][1]-coin[i][1])
    min_v = min(min_v,v)
if min_v==float('inf'):
    ans = -1
else:
    ans = min_v

print(ans)