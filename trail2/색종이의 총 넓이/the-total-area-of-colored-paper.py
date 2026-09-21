n = int(input())
edges = [list(map(int,input().split()))for _ in range(n)]

offset = 100
m = 2*offset + 1
arr = [[0]*m for _ in range(m)]

# Please write your code here.
# 길이가 8이므로 8을 더해주면 된다.
for x1,y1 in edges:
    x1+=offset
    y1+=offset
    for i in range(x1,x1+8):
        for j in range(y1,y1+8):
            arr[i][j]=1

cnt = 0
for i in range(m):
    for j in range(m):
        if arr[i][j]==1:
            cnt+=1


print(cnt)