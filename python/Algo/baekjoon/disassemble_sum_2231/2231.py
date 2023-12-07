N = int(input())

result = []
for i in range(N):
    si = i
    tmp = i
    while True:
        if i == 0:
            break
        tmp += i%10
        i //= 10
    if tmp == N:
        result.append(si)
if result:
    print(result[0])
else:
    print(0)