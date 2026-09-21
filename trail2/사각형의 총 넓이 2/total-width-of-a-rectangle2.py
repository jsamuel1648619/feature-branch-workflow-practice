offset = 100
m = 2*offset +1

arr = [[0]*m for _ in range(m)]

n = int(input())
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())

    x1+=offset
    y1+=offset
    x2+=offset
    y2+=offset
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] =1

cnt = 0 
for i in range(m):
    for j in range(m):
        if arr[i][j] ==1:
            cnt+=1

print(cnt) 
