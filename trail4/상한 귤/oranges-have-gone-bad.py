n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
# Please write your code here.
q = []
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            q.append((i, j))

while q:
    ci, cj = q.pop(0)
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and visited[ni][nj]==0:
            arr[ni][nj] = 2
            visited[ni][nj] += visited[ci][cj] + 1
            q.append((ni, nj))

for i in range(n):
    for j in range(n):
        # 방문을 못 했는데
        if visited[i][j]==0:
            # 처음부터 빈 칸이면
            if arr[i][j]==0:
                visited[i][j]=-1
            # 귤이 들어있는 칸이면
            if arr[i][j]==1:
                visited[i][j]=-2

for row in visited:
    print(*row)