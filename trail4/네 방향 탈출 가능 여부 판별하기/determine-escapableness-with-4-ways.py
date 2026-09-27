n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0]*m for _ in range(n)]
que = [[0,0]]
ans = 0
while que:
    ci,cj = que.pop(0)

    if ci == n-1 and cj == m-1:
        ans = 1
        break

    if visited[ci][cj]==0:
        visited[ci][cj]=1

        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj=ci+di,cj+dj
            # 인덱스 범위를 만족하고
            if 0<=ni<n and 0<=nj<m:
                # 방문 안 했고, 뱀이 없으면
                if visited[ni][nj]==0 and a[ni][nj]==1:
                    que.append([ni,nj])

print(ans)
    
