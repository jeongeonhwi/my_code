cnt = int(input())
ans = ''
for i in range(cnt):
    data = list(input())
    if ans == '':
        ans = data
    else:
        for j in range(len(ans)):
            if ans[j] != data[j]:
                ans[j] = '?'
print(''.join(ans))