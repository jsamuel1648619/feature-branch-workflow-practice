# 격자의 크기, 리브로수를 키우는 총 년 수
n,m = map(int,input().split())
# 서로 다른 리브로수의 높이
arr = [list(map(int,input().split()))for _ in range(n)]
# 각 년도의 이동 규칙
rule = [list(map(int,input().split()))for _ in range(m)]
# d = 이동방향, 이동 칸 수=p

di = [0,-1,-1,-1,0,1,1,1]
dj = [1,1,0,-1,-1,-1,0,1]
#  격자 바깥으로 나가면 마치 지구가 둥근것처럼 반대편으로 돌아옵니다
#  높이가 0인 리브로수는 씨앗만 존재하는 땅을 의미합니다.
# 1. 초기 특수 영양제의 위치 지정 - 완료
q = []
special = [[0]*n for _ in range(n)]
for r in range(n-2,n):
    for c in range(0,2):
        special[r][c]=1
        q.append((r,c))
# 2. 이동 규칙에 따라 이동
for d,p in rule:
    move = []
    q2 = []
    special = [[0] * n for _ in range(n)]
    while q:
        ci,cj = q.pop(0)
        # 새로운 위치로 옮기기
        # d = 0~7, 입력값 = 1~8
        # 지구는 둥그니까...
        ni,nj=(ci+di[d-1]*p)%n,(cj+dj[d-1]*p)%n
        # 새로운 위치로 옮겼어
        special[ni][nj]=1
        # 이동한 좌표 저장
        move.append((ni,nj))

    # 이동했으니 조건 수행
    for r,c in move:
        arr[r][c]+=1
    for r,c in move:
        t_cnt=0
        # 조건을 만족하는 대각선에 인접한 리브로수의 수
        for t in range(0,8,2):
            # 대각선에 인접해 있는지 확인
            ti,tj = r+di[t+1],c+dj[t+1]
            if 0<=ti<n and 0<=tj<n and arr[ti][tj]>=1:
                t_cnt+=1
        # 조건을 만족하는 만큼 더 성장
        arr[r][c]+=t_cnt

    # 높이가 2 이상인 리브로수를 베어서 특수영양제를 만들자.
    for i in range(n):
        for j in range(n):
            if special[i][j]==0 and arr[i][j]>=2:
                arr[i][j]-=2
                q2.append((i,j))
    q=q2

ans=0
for a in range(n):
    for b in range(n):
        ans+=arr[a][b]
print(ans)