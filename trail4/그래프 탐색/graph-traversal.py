n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Please write your code here.
visited = [0]*(n+1)
adj_lst = [[] for _ in range(n + 1)]
cnt = 0
for i in range(m):
    v,w= edges[i]
    adj_lst[v].append(w)
    adj_lst[w].append(v)
    
stack = [1]
while stack:
    a = stack.pop()
    # 방문하지 않았으면
    if visited[a]==0:
        # 방문 표시 
        visited[a]=1
        # 다음으로 갈 수 있는 경우
        for w in adj_lst[a]:
            # 방문하지 않고 스택에도 없으면
            if visited[w]==0 and w not in stack:
                stack.append(w)
                # 새로운 정점을 찾았으므로
                cnt+=1


print(cnt)