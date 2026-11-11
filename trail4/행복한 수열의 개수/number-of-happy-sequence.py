'''
1 이상 100 이하의 정수로만 이루어져 있는 N×N 크기의 격자 정보가 주어집니다.

이때 행복한 수열은 다음과 같이 정의됩니다.

행복한 수열: 동일한 원소가 연속하여 M개 이상 나오는 구간이 존재하는 수열

각 행을 왼쪽에서 오른쪽으로 읽어 얻어지는 N개의 수열과

각 열을 위에서 아래로 읽어 얻어지는 N개의 수열,

총 2N개의 수열 중 행복한 수열의 개수를 세서 출력하는 프로그램을 작성해 주세요.

예를 들어, M=2이고 격자가 다음과 같은 경우라면,

첫 번째 행을 골랐을 경우와 첫 번째 열을 골랐을 경우에만 행복한 수열이 되므로,

총 행복한 수열의 수는 2개가 됩니다.
'''
n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

# 세로탐색 |
cnt = 0
for j in range(n):
    cnt_i = 1
    for i in range(n-1):
        if arr[i][j]==arr[i+1][j]:
            cnt_i += 1
        else:
            cnt_i = 1
        if cnt_i >= m:
            cnt+=1
            break


# 가로탐색 -
for i in range(n):
    cnt_j = 1
    for j in range(n-1):
        if arr[i][j]==arr[i][j+1]:
            cnt_j += 1
        else:
            cnt_j = 1
        if cnt_j >= m:
            cnt+=1
            break

if m==1:
    cnt = 2*n

print(cnt)