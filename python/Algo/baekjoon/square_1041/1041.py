import sys

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

three = sum(arr)
two = three
one = min(arr)

for a,b,c in [(0,1,2),(0,1,3),(0,2,4),(0,3,4),(5,1,3),(5,1,2),]