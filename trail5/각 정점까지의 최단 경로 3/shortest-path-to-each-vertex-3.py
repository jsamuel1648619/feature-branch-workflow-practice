'''
N개의 정점이 존재하고 M개의 간선의 양 끝 정점과 가중치가 주어질 때,

1번 정점에서 다른 모든 정점으로 가는 최단 경로를 구하는 프로그램을 작성해보세요.

이때 주어지는 정점과 간선들로 구성되는 그래프는 단방향 그래프라고 가정합니다.
'''
import heapq

n,m = map(int,input().split())

lst = [[] for _ in range(n+1)]
for _ in range(m):
    # 시작, 끝, 가중치
    a,b,c = map(int,input().split())

    lst[a].append((c,b))

dij = [10000]*(n+1)
dij[1]=0

pq = [(0,1)]

while pq:
    total, start = heapq.heappop(pq)
    if dij[start] < total:
        continue

    for w, g in lst[start]:
        new_cost = total + w
        if dij[g] > new_cost:
            dij[g] = new_cost
            heapq.heappush(pq, (new_cost, g))

for i in range(2,n+1):
    if dij[i]==10000:
        dij[i]=-1
    print(dij[i])