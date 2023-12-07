import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    arr = input()
    check = 0
    for i in arr:
        if i == '(':
            check+=1
        elif i == ')':
            check-=1
        if check < 0:
            break
    if check == 0:
        print('YES')
    else:
        print('NO')
