N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
people = []

stack = []
v_cnt = 0

for i in range(N):
    for j in range(N):

        # 아직 방문하지 않은 집 발견 → 새로운 마을 시작
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            stack.append([i, j])

            p_cnt = 1

            # 현재 마을 탐색
            while stack:
                ci, cj = stack.pop()

                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni = ci + di
                    nj = cj + dj

                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            stack.append([ni, nj])
                            p_cnt += 1

            # 한 마을 탐색 완료
            people.append(p_cnt)
            v_cnt += 1

print(v_cnt)

people.sort()

for i in range(len(people)):
    print(people[i])