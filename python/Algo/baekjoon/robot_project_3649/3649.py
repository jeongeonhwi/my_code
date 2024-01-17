import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def check(start, end):
    stmp = lego[start]+lego[end]
    etmp = lego[start]+lego[end]
    ss,se = start,end
    es,ee = start,end
    while ss>= 0:
        ss-=1
        if x == stmp:
            return (ss,se)
        elif x < stmp:
            return (-1,-1)
    while ee>= 0:
        ee+=1
        if x == etmp:
            return (es,ee)
        elif x < etmp:
            return (-1,-1)
    return (-1,-1)


# 1cm = 10000000nano
x = int(input())
n = int(input())
lego = [int(input()) for _ in range(n)]
x *= 10000000
lego.sort()
start, end = 0, n-1
while start<end+1:
    tmp = lego[start]+lego[end]
    if x == tmp and start != end:
        print(f'yes {lego[start]} {lego[end]}')
        exit()
    elif x > tmp:
        start += 1
    else:
        end -= 1
print('danger')