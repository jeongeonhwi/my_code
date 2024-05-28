import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

data = input().strip()
bomb = input().strip()
bomb_length = len(bomb)
stack = []

for d in data:
    stack.append(d)
    if stack[-bomb_length:] == list(bomb):
        for b in range(bomb_length):
            stack.pop()
print("".join(stack) if stack else "FRULA")