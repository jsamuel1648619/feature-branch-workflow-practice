m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
# m2월 d2일까지 몇일? b
# m1월 d1일까지 몇일? a
# ans = b-a
b = d2
for i in range(1,m2):
    if i in [1,3,5,7,8,10,12]:
        b+= 31
    elif i==2:
        b+= 28
    else:
        b+=30
a = d1
for i in range(1,m1):
    if i in [1,3,5,7,8,10,12]:
        a+= 31
    elif i==2:
        a+= 28
    else:
        a+=30

ans = b-a+1
print(ans)
