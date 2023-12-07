import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fake = []
    for _ in range(N):
        arr = list(input())
        if len(fake) == 0 and arr.count('0') != M:
            fake = arr
    idx = -1
    count = 0
    for i in range(M):
        if idx == -1 and fake[i] != '0':
            idx = i
        if fake[i] != '0':
            count += 1

    code = fake[idx:idx+count]
    hstr = ''.join(code)
    dint = int(hstr, 16)
    bstr = format(dint, 'b')
    a = list(map(str, bstr))
    while True:
        b = a.pop()
        if b != '0':
            a.append(b)
            break
    while True:
        pass