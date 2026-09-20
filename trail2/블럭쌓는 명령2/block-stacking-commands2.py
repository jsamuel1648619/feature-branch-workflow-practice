n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

cnt = [0]*(n+1)

for i in range(k):
    a,b = commands[i]
    for j in range(a,b+1):
        cnt[j]+=1

ans = max(cnt)
print(ans)