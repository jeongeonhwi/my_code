N = [1,2,3,4]
nset = {(tuple(N),1)}

a = [1,2,3,4]


if (tuple(a), 1) in nset:
    print(type((tuple(a), 1)))