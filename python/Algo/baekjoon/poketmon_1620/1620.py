import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
monster = []
num = 1
md = {}
for _ in range(N):
    data = input().strip()
    monster.append(data)
    md[data] = num
    num += 1
for _ in range(M):
    input_data = input().strip()
    try:
        data = int(input_data)
        print(monster[data-1])
    except:
        print(md[input_data])