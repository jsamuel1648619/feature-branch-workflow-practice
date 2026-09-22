n,m,k = map(int,input().split())

penalty = [int(input()) for _ in range(m)]

cnt = [0]*(n+1)

ans = -1
for p in penalty:
    cnt[p]+=1
    if cnt[p]>=k:
        ans = p
        break

print(ans)