
cnt_a = [0]*10000001
cnt_b = [0]*10000001

n,m = map(int,input().split())

a = [input().split() for _ in range(n)]
b = [input().split() for _ in range(m)]

cur_a = 0
time_a = 1
for ad,at in a:
    at = int(at)
    for _ in range(at):
        if ad == 'R':
            cur_a+=1
        else:
            cur_a-=1
        
        cnt_a[time_a] = cur_a
        time_a +=1

time_b = 1
cur_b = 0
for bd,bt in b:
    bt = int(bt)
    for _ in range(bt):
        if bd == 'R':
            cur_b+=1
        else:
            cur_b-=1
        
        cnt_b[time_b] = cur_b
        time_b +=1
ans = -1
for time in range(1,time_a):
    if cnt_a[time]==cnt_b[time]:
        ans = time
        break

print(ans)


# 내가 구현하려고 한 거는
# 일단 cur이라는 변수를 통해서 현재 위치를 담고
# 포문 안에서 cur에 1을 더하거나 빼는 방식으로 저장하려고 했어
# 그리고 카운팅 배열을 만들어서 각 초마다 A와 B의 위치를 저장하려고 했어
# A와 B가 움직인 시간은 같다.


# Please write your code here.