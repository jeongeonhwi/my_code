N = int(input())
my = {1:0, 2:1, 3:1, 4:2, 5:3}
if N == 1:
    print(0)
elif N == 2:
    print(1)
elif N == 3:
    print(1)
elif N == 4:
    print(2)
elif N == 5:
    print(3)
else:
    for i in range(6, N+1):
        my[i] = my[i-1]+1
        if i%3 == 0:
            my[i] = min(my[i//3]+1,my[i])
        if i%2 == 0:
            my[i] = min(my[i//2]+1,my[i])
    print(my[N])