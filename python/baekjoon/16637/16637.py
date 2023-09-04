import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = []
a_str = input()
for i in range(len(a_str)):
    if i%2==0:
        arr.append(int(a_str[i]))
    else:
        arr.append(a_str[i])

