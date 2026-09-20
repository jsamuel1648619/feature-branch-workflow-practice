n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
offset =100
cnt = [0]*201
for a,b in segments:
    a,b= a+offset,b+offset
    for j in range(a,b):
        cnt[j]+= 1
# 선분이 끝에서만 닿는 경우는 겹치는 것으로 생각하지 않는다.
# b+1->b
ans = max(cnt)
print(ans)