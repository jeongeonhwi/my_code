import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N , arr= map(int, input().split())
    arr = list(str(arr))
    stack = []
    stack.append(arr[0])
    for i in range(1, len(arr)):
        if stack:
            if stack[-1] == arr[i]:
                stack.pop()
            else:
                stack.append(arr[i])
        else:
            stack.append(arr[i])
    while stack[0] == '0':
        stack.pop(0)
    result = ''.join(stack)
    print(f'#{tc} {result}')
