n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
que = []
visited = [[0]*(n+1) for _ in range(n+1)]

cnt = 0
for r,c in points:
    r-=1
    c-=1
    if visited[r][c]==0:
        que.append([r,c])
        visited[r][c]=1
        cnt+=1
        while que:
            ci,cj = que.pop(0)
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni,nj = ci+di,cj+dj
                if 0<=ni<n and 0<=nj<n:
                    if visited[ni][nj]==0 and grid[ni][nj]==0:
                        visited[ni][nj]=1
                        que.append([ni,nj])
                        cnt+=1

print(cnt)
                    
        




