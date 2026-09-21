# 가로 길이를 완전히 덮거나 
# 세로 길이를 덮지 않는 한
# A 직사각형 넓이 그대로이다.

offset =1000
m = 2*offset +1

arr = [[0]*m for _ in range(m)]
for k in range(1,3):
    x1,y1,x2,y2 = map(int,input().split())

    x1+=offset
    y1+=offset
    x2+=offset
    y2+=offset

    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] = k
    
max_i,min_i,max_j,min_j = 0,m,0,m
rect_A_exist = False
for i in range(m):
    for j in range(m):
        if arr[i][j]==1:
            rect_A_exist = True
            max_i = max(max_i,i)
            min_i = min(min_i,i)
            max_j = max(max_j,j)
            min_j = min(min_j,j)

if not rect_A_exist:
    area = 0
else:
    area = (max_i-min_i+1)*(max_j-min_j+1)

print(area)
            
    