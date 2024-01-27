import sys
sys.stdin = open('input.txt', 'r')

a,b,c,d,e,f = map(int, input().split())

for i in range(-999, 1000):
    # print(d*((b*i-c)//a) + e*i, f)
    if a == 0:
        y = c//b
        x = (f-e*y)//d
        print(x,y)
        break
    elif d*((c-b*i)/a) + e*i == f:
        print(int((c-b*i)/a), i)
        break