m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
def mon_day(m,d):
    total = d
    for i in range(1,m):
        if i in [1,3,5,7,8,10,12]:
            total+=31
        elif i ==2:
            total+=28
        else:
            total+=30
    return total

a = mon_day(m2,d2)
c = mon_day(m1,d1)
# b = a%7 #4 b= 4일 때 요일은 sun
# d = c%7  #5 d= 5일  때 요일은 mon
b = a - c

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print(days[b % 7])