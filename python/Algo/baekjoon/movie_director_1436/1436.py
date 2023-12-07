import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
c = 0
ans = 0
cnt = 0
while True:
    if str(cnt).count('666') >=1:
        c+=1
    if c == N:
        ans = cnt
        break
    cnt += 1
print(ans)