import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
set_arr = list(set(arr))
set_arr.sort()
num = dict()
for i in range(len(set_arr)):
    num[set_arr[i]] = i
ans = []
for i in arr:
    ans.append(num[i])
print(*ans)