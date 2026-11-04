n = int(input())
cnt5 = n//5
coin = n%5
cnt2 = coin //2
coin %= 2
ans = -1
# 초기의 coin 값은 무조건 0또는 1
if coin:
    # cnt5가 0이 아니어야
    if cnt5:
        cnt5-=1
        cnt2+=3
        ans = cnt5+cnt2

else:
    ans = cnt5+cnt2
print(ans)