import sys
sys.stdin = open('input.txt', 'r')

def my_perm(time):
    global max_v
    value = int(''.join(numbers))
    if value in checked[time]:
        return
    checked[time].add(value)
    if time == L:
        if max_v < value:
            max_v = value
        return
    else:
        for i in range(N):
            for j in range(i+1, N):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                my_perm(time+1)
                numbers[i], numbers[j] = numbers[j], numbers[i]



T = int(input())
for tc in range(1, T+1):
    numbers, L = input().split()
    numbers = list(numbers)
    N = len(numbers)
    L = int(L)
    checked = [set() for _ in range(11)]
    max_v = 0
    my_perm(0)
    print(f'#{tc} {max_v}')
