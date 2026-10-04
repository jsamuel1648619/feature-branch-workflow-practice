n, r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

r, c = r-1, c-1

# 우리 델타 기준
# 0 = 우, 1 = 하, 2 = 좌, 3 = 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 문제 방향
# 1 = 상, 2 = 하, 3 = 좌, 4 = 우
dir_map = [3, 1, 2, 0]
d = dir_map[d-1]

visited = [[0] * n for _ in range(n)]
visited[r][c] = 1

ans = [(r, c)]

q1 = [(r, c, d)]

while True:

    # =========================
    # 1단계
    # 인접한 미방문 바다 탐험
    # =========================
    while q1:
        ci, cj, cd = q1.pop(0)

        # 직진 -> 좌회전 -> 우회전 -> 뒤
        dirs = [
            cd,
            (cd + 3) % 4,
            (cd + 1) % 4,
            (cd + 2) % 4
        ]

        for nd in dirs:
            ni = ci + di[nd]
            nj = cj + dj[nd]

            if (0 <= ni < n and 0 <= nj < n
                    and arr[ni][nj] == 0
                    and visited[ni][nj] == 0):

                visited[ni][nj] = 1
                ans.append((ni, nj))

                # 이동한 방향으로 갱신
                q1.append((ni, nj, nd))
                break


    # =========================
    # 2단계
    # 가장 가까운 미방문 바다 찾기
    # =========================
    cand = []

    distance = [[-1] * n for _ in range(n)]
    distance[ci][cj] = 0

    q2 = [(ci, cj)]

    while q2:
        cr, cc = q2.pop(0)

        for nd in range(4):
            nr = cr + di[nd]
            nc = cc + dj[nd]

            if (0 <= nr < n and 0 <= nc < n
                    and arr[nr][nc] == 0
                    and distance[nr][nc] == -1):

                distance[nr][nc] = distance[cr][cc] + 1
                q2.append((nr, nc))

                if visited[nr][nc] == 0:
                    cand.append((distance[nr][nc], nr, nc))


    # 갈 수 있는 미방문 바다가 없음
    if not cand:
        break

    # 거리 -> 행 -> 열
    cand.sort()
    dist, tr, tc = cand[0]


    # =========================
    # 목적지 기준 역방향 BFS
    # =========================
    back = [[-1] * n for _ in range(n)]
    back[tr][tc] = 0

    q3 = [(tr, tc)]

    while q3:
        cr, cc = q3.pop(0)

        for nd in range(4):
            nr = cr + di[nd]
            nc = cc + dj[nd]

            if (0 <= nr < n and 0 <= nc < n
                    and arr[nr][nc] == 0
                    and back[nr][nc] == -1):

                back[nr][nc] = back[cr][cc] + 1
                q3.append((nr, nc))


    # =========================
    # 목적지까지 실제 이동
    # 좌 -> 하 -> 우 -> 상
    # =========================
    mr, mc = ci, cj
    last_d = cd

    while (mr, mc) != (tr, tc):

        for nd in [2, 1, 0, 3]:
            nr = mr + di[nd]
            nc = mc + dj[nd]

            if (0 <= nr < n and 0 <= nc < n
                    and back[nr][nc] == back[mr][mc] - 1):

                mr, mc = nr, nc
                last_d = nd

                # 처음 방문한 바다만 기록
                if visited[mr][mc] == 0:
                    visited[mr][mc] = 1
                    ans.append((mr, mc))

                break

    # 목적지 도착 후 마지막 이동 방향 유지
    q1.append((mr, mc, last_d))


# 1-index 복구
for i, j in ans:
    print(i + 1, j + 1)