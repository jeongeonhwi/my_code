n,k = map(int, input().split())
arr = input().strip()
arr *= k
ans = 'NO'
d = {U:(-1,0), L:(0,-1), R:(0,1), D:(1,0)}
si,sj = d[arr[0]]
for i in range(1, len(arr)):
    si,sj = si+d[arr[i]][0], sj+d[arr[i]][1]
    if si == 0 and sj == 0:
        ans = 'YES'
        break
print(ans)