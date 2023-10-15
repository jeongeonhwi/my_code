from itertools import combinations

a = [(1,1),(1,3),(1,5)]

combi = set(combinations(a,2))
for i in combi:
    for j in i:
        if (j[0],j[1]+2) in i:
            print('yes')
            print(j, i)
