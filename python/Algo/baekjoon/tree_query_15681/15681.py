import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def makeTree(currentNode, parent):
    for node in arr[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            nodelist[node] = currentNode
            makeTree(node, currentNode)

def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for node in child[currentNode]:
        countSubtreeNodes(node)
        size[currentNode] += size[node]

N, R, Q = map(int, input().split())
nodelist = [i for i in range(N+1)]
child = [[] for _ in range(N+1)]
size = [1 for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

makeTree(R,-1)
countSubtreeNodes(R)
print(size)
for _ in range(Q):
    data = int(input())
    print(size[data])
