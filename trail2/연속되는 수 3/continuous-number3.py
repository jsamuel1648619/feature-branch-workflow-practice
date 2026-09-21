n = int(input())
arr = [int(input()) for _ in range(n)]


# Please write your code here.
max_cnt = 1
for i in range(n):
    if i >= 1 and arr[i]*arr[i-1]>0:
        cnt += 1
    # Case 2
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)