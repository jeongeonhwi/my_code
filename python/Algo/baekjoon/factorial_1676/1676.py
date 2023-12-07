N = int(input())

numbers = [i for i in range(1, N+1)]
ans = 1
for i in numbers:
    ans *= i
result = 0
str_ans = str(ans)
c = len(str_ans)-1
for i in range(c, -1, -1):
    if str_ans[i] == '0':
        result += 1
    else:
        break
print(result)