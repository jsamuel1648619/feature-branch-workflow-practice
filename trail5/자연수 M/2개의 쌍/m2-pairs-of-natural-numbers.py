# 변수 선언 및 입력:
n = int(input())
ans = 0

nums = []
for _ in range(n):
    x, y = tuple(map(int, input().split()))
    nums.append((y, x))

# y 기준으로 오름차순 정렬을 진행합니다.
nums.sort()

# 최선의 전략을 오름차순 정렬 뒤
# 가장 작은 수와 큰 수를 하나씩 매칭해주는 것입니다.
li, ri = 0, n - 1
while li <= ri:
    ly, lx = nums[li]
    ry, rx = nums[ri]

    # 답을 갱신합니다.
    ans = max(ans, ly + ry)

    # 왼쪽 개수가 더 적다면
    # 왼쪽을 전부 매칭시켜줍니다.
    if lx < rx:
        # 오른쪽은 lx만큼 개수를 줄여줍니다.
        nums[ri] = (ry, rx - lx)
        # 왼쪽 위치를 한칸 뒤로 옮겨줍니다.
        li += 1

    # 오른쪽 개수가 더 적다면
    # 오른쪽을 전부 매칭시켜줍니다.
    elif lx > rx:
        # 왼쪽은 rx만큼 개수를 줄여줍니다.
        nums[li] = (ly, lx - rx)
        # 오른쪽 위치를 한칸 앞으로 옮겨줍니다.
        ri -= 1

    # 개수가 동일하다면
    # li, ri 위치 모두 옮겨줍니다.
    else:
        li += 1
        ri -= 1

print(ans)
