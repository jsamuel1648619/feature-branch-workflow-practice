n = int(input())
arr = [int(input()) for _ in range(n)]


# Please write your code here.
max_cnt = 1
for i in range(n):
    cnt = 1
    for j in range(i+1,n):
        if arr[i]*arr[j]>0:
            cnt +=1
            max_cnt = max(max_cnt,cnt)
        else:
            break

print(max_cnt)