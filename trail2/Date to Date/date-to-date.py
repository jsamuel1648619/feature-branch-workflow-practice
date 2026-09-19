m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
# m2월 d2일까지 몇일? b
# m1월 d1일까지 몇일? a
# ans = b-a
def mon_day(m,d):
    total = d
    for i in range(1,m):
        if i in [1,3,5,7,8,10,12]:
            total+= 31
        elif i==2:
            total+= 28
        else:
            total+=30 
    return total

ans = mon_day(m2,d2)-mon_day(m1,d1)+1
print(ans)
