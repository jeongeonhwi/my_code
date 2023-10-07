import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

arr = []
while True:
    a = int(input())
    if not a:
        break
    arr.append(list(str(a)))
for i in arr:
    cnt = 0
    for j in range(len(i)//2):
        if i[j] == i[len(i)-1-j]:
            cnt += 1
    if cnt == len(i)//2:
        print('yes')
    else:
        print('no')