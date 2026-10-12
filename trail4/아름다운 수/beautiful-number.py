# 1이상 4이하의 정수로만 이루어져 있으면서,
# 정확히 해당 숫자만큼 연달아 같은 숫자가 나오는 수를 아름다운 수
# N자리 아름다운 수가 몇 개 있는지를 구하는 프로그램을 작성
# n자리 수
def make_arr(level):
    global ans
    if level==n:
        if find_beaut(num)==True:
            ans+=1
        return
    for k in range(1,5):
        num.append(k)
        make_arr(level+1)
        num.pop()


def find_beaut(lst):
    m = len(lst)
    i = 0
    while i<m:
        elem = lst[i]
        cnt = 0
        while i<m and lst[i]==elem:
            cnt+=1
            i+=1

        if cnt%elem!=0:
            return False
    return True


n = int(input())

num =[]
ans = 0
make_arr(0)
print(ans)

