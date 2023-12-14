import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


while True:
    data = input()
    if data == '.':
        break
    # print(data)
    small = 0
    big = 0
    stack = []
    for i in data:
        if i == '(':
            small += 1
            stack.append('(')
            continue
        if i == ')':
            small -= 1
            if stack:
                check = stack.pop()
                if check != '(':
                    print('no')
                    break
            else:
                print('no')
                break
            if small < 0:
                print('no')
                break
            continue
        if i == '[':
            big += 1
            stack.append('[')
            continue
        if i == ']':
            big -= 1
            # print(stack)
            if stack:
                check = stack.pop()
                if check != '[':
                    print('no')
                    break
            else:
                print('no')
                break
            if big < 0:
                print('no')
                break
            continue
    else:
        if small == 0 and big == 0:
            print('yes')
        else:
            print('no')