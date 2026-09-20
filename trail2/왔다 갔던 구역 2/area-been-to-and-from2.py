n = int(input())

offset = 1000
cnt = [0]*2001

cur = 0
distance = []
for _ in range(n):
    xi,dir = input().split()
    xi = int(xi)

    if dir == 'L':
        left = cur - xi
        right = cur
        cur-=xi
    else: # dir == 'R'
        left = cur
        right = cur+xi
        cur+=xi
    distance.append([left,right])

for l,r in distance:
    l,r = l+offset,r+offset

    for i in range(l,r):
        cnt[i]+=1

area = 0
for c in cnt:
    if c>=2:
        area+=1

print(area)