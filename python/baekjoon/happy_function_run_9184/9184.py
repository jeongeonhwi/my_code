import sys
sys.stdin = open('input.txt', 'r')

arr = []
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    arr.append((a, b, c))
