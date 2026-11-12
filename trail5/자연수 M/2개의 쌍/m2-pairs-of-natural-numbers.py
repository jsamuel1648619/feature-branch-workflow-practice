'''
M개의 자연수가 있습니다. 이 자연수들을 두 개씩 짝지어

M/2개의 쌍을 만들려고 합니다.

M/2개의 쌍들 중 두 자연수의 합이 가장 큰 쌍의 두 자연수 합을 C라고 할 때,

가능한 C의 최솟값을 구하는 프로그램을 작성해보세요.
'''


n = int(input())
nums = []

for _ in range(n):
    a,b = map(int,input().split())

    nums.append([b,a])

nums.sort()
# print(nums)

ans = 0
left = 0
right = n-1

while left <= right:
    lb,la = nums[left]
    rb,ra = nums[right]

    ans = max(ans,lb+rb)
    if la>ra:
        nums[left] = [lb,la-ra]
        # 오른쪽에 남은 개수가 없으므로 포인터 이동
        right-=1
    elif la<ra:
        nums[right] = [rb,ra-la]
        # 왼쪽에 남은 개수가 없으므로 포인터 이동
        left+=1
    else:
        left +=1
        right -=1

print(ans)