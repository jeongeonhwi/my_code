import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

data = int(input())

def checkOne(num):
    check = num
    defference = 10000
    while True:
        one = check%10
        check //= 10
        two = check % 10
        if check == 0:
            return True
        if defference == 10000:
            defference = one - two
        else:
            if defference != one-two:
                return False

ans = 0
for i in range(1, data+1):
    ans += checkOne(i)
print(ans)