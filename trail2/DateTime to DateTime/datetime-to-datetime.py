a, b, c = map(int, input().split())

# Please write your code here.

# 11월 11일 0시 0분에 시작해서

# A*60*24 + B*60+ C - 11*60+11 계산
if (a*60*24 + b*60+ c) - (11*60*24 +11*60+ 11) < 0:
    print(-1)
else:
    print((a*60*24 + b*60+ c) - (11*60*24 +11*60+ 11))

