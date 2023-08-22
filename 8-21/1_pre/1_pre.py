import sys
sys.stdin = open('input.txt')

def preorder(n):
    if n:
        visited.append(n)
        preorder(ch1[n])
        preorder(ch2[n])


V = int(input())
E = V-1
arr = list(map(int, input().split()))
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
par = [0]*(V+1)
visited = []
for i in range(E):
    if ch1[arr[i*2]] == 0:
        ch1[arr[i*2]] = arr[i*2+1]
    else:
        ch2[arr[i*2]] = arr[i*2+1]
    par[arr[i*2+1]] = arr[i*2]
# print(par)

root = 1
while par[root] != 0:
    root += 1

preorder(root)
print(*visited)