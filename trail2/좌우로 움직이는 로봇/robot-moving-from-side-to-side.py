n, m = map(int,input().split())

info_a = [input().split() for _ in range(n)]
info_b = [input().split() for _ in range(m)]

# 직전에는 서로 다른 위치에 있다가 같은 위치에서 만나는 횟루르 출력.

offset = 2000001

pos_a = [0]*offset
time_a = 1
for t,d in info_a:
    t = int(t)
    for _ in range(t):
        if d == 'R':
            pos_a[time_a] = pos_a[time_a-1]+1
        else:
            pos_a[time_a] = pos_a[time_a-1]-1
        time_a+=1

pos_b = [0]*offset
time_b = 1
for t,d in info_b:
    t = int(t)
    for _ in range(t):
        if d == 'R':
            pos_b[time_b] = pos_b[time_b-1]+1
        else:
            pos_b[time_b] = pos_b[time_b-1]-1
        time_b+=1

# 각 로봇이 움직임을 종료한 이후에는 같은 위치에 계속 머물러 있으며
# 이때 역시 다른 로봇이 움직임에 따라 두 로봇이 같은 위치에 오게 될 수 있습니다.s = 0
max_time = max(time_a, time_b)

for t in range(time_a, max_time + 1):
    pos_a[t] = pos_a[time_a - 1]

for t in range(time_b, max_time + 1):
    pos_b[t] = pos_b[time_b - 1]

ans = 0
for time in range(max(time_a,time_b)):
    if pos_a[time]!=pos_b[time] and pos_a[time+1]==pos_b[time+1]:
        ans+=1

print(ans)