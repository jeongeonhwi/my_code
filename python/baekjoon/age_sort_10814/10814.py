import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N = int(input())
number = [[] for _ in range(201)]
for _ in range(N):
    data = list(map(str, input().strip().split()))

    age, name = int(data[0]), data[1]
    number[age].append(data)
for i in number:
    if len(i) == 1:
        print(*i[0])
    elif len(i) > 1:
        for ii in i:
            print(*ii)


# sort 사용한 버전
# N = int(input())
# number = []
# c = 1
# for _ in range(N):
#     data = list(map(str, input().split(' ')))
#     age, name = int(data[0]), data[1]
#     number.append((age, name, c))
#     c += 1
# number.sort(key=lambda x: x[0])
# for i in number:
#     print(f'{i[0]} {i[1]}')