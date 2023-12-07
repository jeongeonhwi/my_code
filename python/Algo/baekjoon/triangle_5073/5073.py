import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

arr  = []
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    arr.append([a,b,c])
for triangle in arr:
    if triangle[0] >= triangle[1] + triangle[2] or triangle[1] >= triangle[0] + triangle[2] or triangle[2] >= triangle[1] + triangle[0]:
        print('Invalid')
    elif triangle[0] == triangle[1] and triangle[1] == triangle[2]:
        print('Equilateral')
    elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0] == triangle[2]:
        print('Isosceles')
    elif triangle[0] != triangle[1] and triangle[1] != triangle[2]:
        print('Scalene')
