'''
N×N 크기의 격자 정보가 주어집니다.
이때 해당 위치에 동전이 있다면 1, 없다면 0이 주어집니다.
N×N 격자를 벗어나지 않도록
연속한 3개의 행과
연속한 3개의 열이 이루는
 3×3 크기의 부분 격자를
 적절하게 잘 잡아서
 해당 범위 안에 들어있는 동전의 개수를 최대로 하는 프로그램을 작성해보세요.
'''

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

max_cnt = cnt = 0

# 조졌네 까먹었어
# for i in range(n):
#     for j in range(n):
#         if arr[i][j]==1:
#             cnt += 1

for i in range(n-2):
    for j in range(n-2):
        cnt = 0
        for r in range(i,i+3):
            for c in range(j,j+3):
                if arr[r][c]==1:
                    cnt+=1
        
        max_cnt = max(max_cnt,cnt)
        
print(max_cnt)
