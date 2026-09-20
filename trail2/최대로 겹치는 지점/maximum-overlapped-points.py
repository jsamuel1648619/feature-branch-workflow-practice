n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cnt = [0]*101

for a,b in segments:
    for j in range(a,b+1):
        cnt[j]+=1

ans = max(cnt)
print(ans)