n, h, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.
people =[[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        visited = [[0]*n for _ in range(n)]
        if arr[i][j]==2:
            visited[i][j]=1
            people[i][j]=-1
            que=[[i,j]]
            
            while que:
                ci,cj=que.pop(0)

                if arr[ci][cj]==3:
                    people[i][j]=visited[ci][cj]-1
                    break

                for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    ni,nj=ci+di,cj+dj
                    if 0<=ni<n and 0<=nj<n:
                        if visited[ni][nj]==0 and arr[ni][nj]!=1:
                            visited[ni][nj] = visited[ci][cj]+1
                            que.append([ni,nj])
                                    
for p in people:
    print(*p)