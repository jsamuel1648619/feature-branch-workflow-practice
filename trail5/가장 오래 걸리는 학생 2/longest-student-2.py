'''
N개의 서로 다른 장소가 있습니다. 1번부터 N−1번 장소에는 학생이 한 명씩 살고 있고,

N번 장소는 학교입니다. 두 개의 장소를 연결하는 간선은 없거나, 있다면 최대 1개만 있으며,

주어지는 모든 간선은 방향성을 갖습니다. 간선마다 길이 d가 주어지며,

각 학생은 등교 시 최단거리로 학교로 이동한다고 합니다.

모든 학생은 거리 1을 이동하는 데 1초의 시간이 걸린다고 했을 때,

학교에 등교하는 데 가장 오래 걸리는 학생의 소요 시간을 구하는 프로그램을 작성해보세요.
'''
import heapq
# 장소의 개수 n, 간선의 개수 m
n,m = map(int,input().split())

lst = [[]for _ in range(n+1)]
for _ in range(m):
    # 시작, 도착, 가중치
    a,b,c = map(int,input().split())

    # lst[a].append((c,b))
    lst[b].append((c,a))

dij = [float('inf')]*(n+1)
dij[n]=0
# 거리:0, 출발:1
# 근데 거꾸로 생각하면, 도착점에서 모든 정점을 방문하는 경우
pq = [(0,n)]
while pq:
    # 거리 합 , 시작정점
    total,start = heapq.heappop(pq)

    if total > dij[start]:
        continue
    # 가중치, 도착정점
    for w,g in lst[start]:
        new_cost = total + w
        if dij[g] > new_cost:
            dij[g]=new_cost
            heapq.heappush(pq,(new_cost,g))

ans = max(dij[1:])
print(ans)