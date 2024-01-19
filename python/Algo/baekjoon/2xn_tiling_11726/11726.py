import sys

desired_recursion_depth = 5000
sys.setrecursionlimit(desired_recursion_depth)




def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input())
if n == 1:
    print(1%10007)
elif n == 2:
    print(2%10007)
else:
    ans = 0
    for i in range(n//2+1):
        one,two = n-i*2, i
        t = n-i
        ans += factorial(t)//(factorial(one)*factorial(two))

    print(int(ans)%10007)