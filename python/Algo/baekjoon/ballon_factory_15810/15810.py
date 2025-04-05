import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


def find_limit():
    pre_cnt = 0
    cnt = 0
    t = 1
    while M<=cnt:
        pre_cnt = cnt
        for s in staff:
            if s <= t:
                cnt+=t//s
            else:
                break
        t*=2
    return pre_cnt, t


N,M = map(int, input().split())
staff = list(map(int, input().split()))
staff.sort()
