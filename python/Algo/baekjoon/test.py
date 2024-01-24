from collections import deque


def find_s_e(board):
    s, e = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                s = (i, j)
            if board[i][j] == 'G':
                e = (i, j)
    return s, e


def bfs(row, col, start, end):
    direction = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
    visited = [[0] * col for _ in range(row)]


def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    start, end = find_s_e(board)
    bfs(row, col, start, end)
    return end