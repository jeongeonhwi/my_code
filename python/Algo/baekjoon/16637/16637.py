import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, value):
    global max_v
    if N == i:
        max_v = max(max_v, int(value))
        return
    if i+4 <= N:
        dfs(i+4, str(eval(''.join([value, arr[i]] + [str(eval(''.join(arr[i+1:i+4])))]))))
    if i+2 <= N:
        dfs(i+2, str(eval(''.join([value] + arr[i:i+2]))))


N = int(input())
arr = list(input())
max_v = float('-inf')
dfs(1, arr[0])
print(max_v)