import sys
sys.stdin = open('input.txt', 'r')

# 파이어볼 정보 i, j, m, 속력, 방향 인덱스들은 마이너스1해줘야함
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

direction = [[-1, 0], [-1, 1], [0, 1], [1,1], [1, 0], [1,-1], [0,-1], [-1, -1]]

