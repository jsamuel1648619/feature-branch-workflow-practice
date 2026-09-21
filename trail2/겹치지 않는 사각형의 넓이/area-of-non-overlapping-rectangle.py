lst = [list(map(int,input().split()))for _ in range(3)]

offset =1000
m = 2*offset + 1

arr = [[0]*m for _ in range(m)]

for k in range(3):
    x1,y1,x2,y2 = lst[k]

    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset
    for i in range(x1,x2):
        for j in range(y1,y2):
            if k==0:
                arr[i][j] = 1
            elif k==1:
                arr[i][j] = 1
            elif k==2:
                arr[i][j] = 2


cnt = 0
for i in range(m):
    for j in range(m):
        if arr[i][j]==1:
            cnt+=1

print(cnt)