import sys
sys.stdin = open('input.txt')

width_total, length_total = map(int, input().split())
num = int(input())
widlist = []
lenlist = []
for _ in range(num):
    style, num = map(int, input().split())
    if style == 0:
        widlist.append(num)
    else:
        lenlist.append(num)
print(widlist)
print(lenlist)