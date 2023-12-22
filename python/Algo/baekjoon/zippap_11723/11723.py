import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = set()
for _ in range(N):
    data = input().strip()
    if data[0:3] == 'che':
        order, num = data.split()
        print(1 if num in arr else 0)
    elif data[0:3] == 'add':
        order, num = data.split()
        arr.add(num)
    elif data[0:3] == 'rem':
        order, num = data.split()
        arr.discard(num)
    elif data[0:3] == 'tog':
        order, num = data.split()
        arr.symmetric_difference_update({num})
    elif data[0:3] == 'all':
        arr = {str(i) for i in range(1, 21)}
    elif data[0:3] == 'emp':
        arr.clear()