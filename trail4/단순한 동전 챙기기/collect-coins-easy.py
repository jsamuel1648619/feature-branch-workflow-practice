def select(level, start):
    if level == 3:
        result.append(move[:])
        return

    for i in range(start, 10):
        move.append(i)
        select(level + 1, i + 1)
        move.pop()


def bfs(start, end):
    q = [start]
    visited = [[-1] * n for _ in range(n)]

    sr, sc = start
    visited[sr][sc] = 0

    while q:
        ci, cj = q.pop(0)

        # 목적지 도착 시 최단거리 반환
        if (ci, cj) == end:
            return visited[ci][cj]

        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]

            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] == -1:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni, nj))

    return -1


n = int(input())
arr = [list(input()) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

move = []
result = []
coin_pos = {}

# 시작점, 도착점, 동전 좌표 저장
for r in range(n):
    for c in range(n):
        if arr[r][c] == 'S':
            start_pos = (r, c)

        elif arr[r][c] == 'E':
            end_pos = (r, c)

        elif arr[r][c].isdigit():
            coin_pos[int(arr[r][c])] = (r, c)

# 동전 3개 조합 생성
select(0, 1)

min_v = float('inf')

# 조합 하나씩 확인
for selected in result:

    # 실제 존재하는 동전인지 검사
    possible = True

    for num in selected:
        if num not in coin_pos:
            possible = False
            break

    if not possible:
        continue

    # S -> 동전1 -> 동전2 -> 동전3 -> E
    q2 = [start_pos]

    for num in selected:
        q2.append(coin_pos[num])

    q2.append(end_pos)

    # 네 구간 BFS 거리 합산
    total = 0

    for i in range(4):
        v = bfs(q2[i], q2[i + 1])

        if v == -1:
            possible = False
            break

        total += v

    # 최소 이동 횟수 갱신
    if possible:
        min_v = min(min_v, total)

# 불가능하면 -1
if min_v == float('inf'):
    print(-1)
else:
    print(min_v)