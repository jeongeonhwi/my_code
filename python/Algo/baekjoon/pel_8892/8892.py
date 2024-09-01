import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from itertools import permutations

def check_pel(tmp):
    lt = len(tmp)
    index = lt//2
    lt -= 1
    for i in range(index):
        if tmp[i] != tmp[lt-i]:
            return False
    return True


T = int(input())
for _ in range(T):
    N = int(input())
    password = []
    for _ in range(N):
        password.append(input().strip())
    for s1,s2 in permutations(password, 2):
        tmp = s1+s2
        if check_pel(tmp):
            print(tmp)
            break
    else:
        print(0)