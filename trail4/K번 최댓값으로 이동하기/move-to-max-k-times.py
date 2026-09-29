n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 1-indexed → 0-indexed
r -= 1
c -= 1

for _ in range(k):

    visited = [[0] * n for _ in range(n)]
    que = [[r, c]]
    visited[r][c] = 1

    # 이번 이동에서 갈 수 있는 칸들
    possible = []

    # 현재 위치의 숫자
    start_num = arr[r][c]

    while que:
        ci, cj = que.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] == 0 and arr[ni][nj] < start_num:
                    visited[ni][nj] = 1
                    que.append([ni, nj])

                    # 이동 가능한 위치 저장
                    possible.append([ni, nj])

    # 더 이상 이동할 곳이 없으면 종료
    if not possible:
        break

    # 갈 수 있는 곳 중 가장 큰 숫자 찾기
    max_num = -1

    for i, j in possible:
        if arr[i][j] > max_num:
            max_num = arr[i][j]

    # 같은 최댓값 중 행 → 열이 작은 위치 선택
    nr = n
    nc = n

    for i, j in possible:
        if arr[i][j] == max_num:
            if i < nr or (i == nr and j < nc):
                nr = i
                nc = j

    # 한 번 이동 완료
    r = nr
    c = nc

print(r + 1, c + 1)