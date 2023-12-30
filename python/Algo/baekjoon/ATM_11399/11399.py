import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
wait = 0
ans = 0
for i in arr:
    wait += i
    ans += wait
print(ans)
