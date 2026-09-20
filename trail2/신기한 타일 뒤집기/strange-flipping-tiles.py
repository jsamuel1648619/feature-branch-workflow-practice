n = int(input())

offset = 100000

cnt = [0]*(2*offset+1)
cur = 0
distance = []
for _ in range(n):
    xi,dir = input().split()
    xi = int(xi)

    if dir == 'R':
        left = cur
        right = cur + xi - 1
        cur += xi - 1
    elif dir == 'L':
        left = cur - xi + 1
        right = cur
        cur -= xi - 1
    distance.append([left,right,dir])

for l,r,d in distance:
    l+=offset
    r+=offset
    for i in range(l,r+1):
        # 검은색으로 바뀜
        if d == 'R':
            cnt[i]=1
        elif d == 'L':
            cnt[i]=-1


cnt_b, cnt_w = 0,0
for c in cnt:
    if c == 1:
        cnt_b +=1
    elif c == -1:
        cnt_w +=1

print(cnt_w,cnt_b)

