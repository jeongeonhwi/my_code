import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    stack = []
    stack.append(arr[0])
    for i in range(1, len(arr)):
        if stack:
            if arr[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(arr[i])
        else:
            stack.append(arr[i])
    print(f'#{tc} {len(stack)}')