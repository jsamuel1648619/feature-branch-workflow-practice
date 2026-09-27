n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 격자의 각 칸의 값은 뱀이 없는 경우 1
# 뱀이 있는 경우 0이다.
visited = [[0] * (m + 1) for _ in range(n + 1)]
stack = [[0, 0]]

ans = 0
while stack:
    r, c = stack.pop()
    # 아래와 오른쪽 두 방향 중 인접한 칸으로만 이동
    for di,dj in [[0,1],[1,0]]:
        ni,nj = r+di,c+dj
        # 인덱스 범위를 만족하는데
        if 0<=ni<n and 0<=nj<m:
            # 아직 방문 안 했고, 뱀이 없으면
            if visited[ni][nj] == 0 and grid[ni][nj] == 1:
                # 방문 처리하고
                visited[ni][nj] = 1
                # 스택에 넣어서 확인
                stack.append([ni, nj])
    # while문을 탈출했지만
    # 마지막 스택에서 나온 값이 [n-1,m-1]이면 탈출가능
    if r == n - 1 and c == m-1:
        ans = 1

print(ans)