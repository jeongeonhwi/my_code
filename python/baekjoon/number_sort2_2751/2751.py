import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N=  int(input())
number = []
for _ in range(N):
    a = int(input())
    number.append(a)
number.sort()
for i in number:
    print(i)