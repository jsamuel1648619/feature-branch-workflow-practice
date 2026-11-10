import heapq

# 정점 개수, 간선 개수
n, m = map(int, input().split())

# 인접 리스트
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    arr[s].append((e, w))
    arr[e].append((s, w))

# 시작점, 도착점
a, b = map(int, input().split())

# 최단거리 및 경로 초기화
INF = float('inf')
dij = [INF] * (n + 1)
paths = [[] for _ in range(n + 1)]

dij[a] = 0
paths[a] = [a]

# (거리, 전체 경로, 현재 정점)
pq = [(0, [a], a)]

while pq:
    cost, path, start = heapq.heappop(pq)

    # 오래된 거리 또는 경로 기록 건너뛰기
    if dij[start] < cost or paths[start] != path:
        continue

    # 도착점에 도달하면 종료
    if start == b:
        break

    for g, w in arr[start]:
        new_cost = cost + w
        new_path = path + [g]

        # 더 짧은 경로 발견
        if new_cost < dij[g]:
            dij[g] = new_cost
            paths[g] = new_path
            heapq.heappush(pq, (new_cost, new_path, g))

        # 거리가 같으면 사전순 비교
        elif new_cost == dij[g] and new_path < paths[g]:
            paths[g] = new_path
            heapq.heappush(pq, (new_cost, new_path, g))

# 출력
print(dij[b])
print(*paths[b])