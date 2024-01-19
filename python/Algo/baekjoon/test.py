n = int(input())
if n == 1:
    print(9)
else:
    ans = 9
    for i in range(2,n+1):
        ans += 2**i*4
    print(ans)