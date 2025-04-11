from itertools import combinations

n,l,r,x = map(int, input().split())
arr = list(map(int, input().split()))
c = 0
for i in range(2,n+1):
    for combi in combinations(arr, i):
        if l<=sum(combi)<=r and max(combi) - min(combi) >= x:
            c+=1
print(c)