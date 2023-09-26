import sys
sys.stdin = open('input.txt', 'r')

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]