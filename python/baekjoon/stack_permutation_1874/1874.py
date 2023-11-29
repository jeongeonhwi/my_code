import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
want_number = [int(input()) for _ in range(N)]
reversed_number = []
for i in range(N-1, -1, -1):
    reversed_number.append(want_number[i])
want_number = reversed_number
# print(want_number)
number = [i for i in range(N, 0, -1)]
stack = []
count = 0
result = []
while number:
    want_pop = want_number.pop()
    number_pop = number.pop()

    stack.append(number_pop)
    want_number.append(want_pop)
    result.append('+')


    if len(stack) > 0:
        while stack:
            stack_pop = stack.pop()
            want_pop = want_number.pop()
            if want_pop == stack_pop:
                result.append('-')
                count += 1
            else:
                stack.append(stack_pop)
                want_number.append(want_pop)
                break

    # print(stack)
    # print(number)

if count < N:
    print('NO')
else:
    for i in result:
        print(i)
# stack.append(number.pop())
# stack.append(number.pop())
# stack.append(number.pop())
# stack.append(number.pop())
# print(stack.pop())
# print(stack.pop())
# stack.append(number.pop())
# stack.append(number.pop())
# print(stack.pop())
# stack.append(number.pop())
# stack.append(number.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(want_number)
# print(stack)