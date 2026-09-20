n = int(input())
offset = 100000

# 이동하기
cur = 0
distance = []
for _ in range(n):
    xi,dir = input().split()
    xi = int(xi)
    if dir == 'R':
        left = cur
        right = cur + xi-1
        cur += xi-1
    else:   # dir =='L'
        left = cur - xi + 1
        right = cur
        cur -= xi-1
    distance.append([left,right,dir])
# 칠하기
# 흰색과 검은색으로 칠하는 경우를 나눠야 함.
# 흰 색 : l>r:-1, 검은색 : l<r:1
# 근데 여기서 마지막으로 칠해진 색으로 바뀌니까...
cnt_b = [0]*(2*offset + 1)
cnt_w = [0]*(2*offset + 1)
last = [0]*(2*offset + 1)
for l,r,dir in distance:
    l+=offset
    r+=offset
    for i in range(l,r+1):
        if last[i]==3:
            continue
        if dir == 'L':
            cnt_w[i] += 1
            last[i]= -1
        elif dir == 'R':
            cnt_b[i] += 1
            last[i] = 1
        if cnt_b[i] >=2 and cnt_w[i] >=2:
            last[i] =3

# 개수 세기
white, black, gray = 0,0,0
for i in range(2*offset+1):
    if last[i] == 1:
        black+=1
    elif last[i]==-1:
        white+=1
    elif last[i]==3:
        gray+=1

print(white, black, gray)