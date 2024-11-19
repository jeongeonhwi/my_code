N = int(input())
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    pipo = [0,1]
    while len(pipo) != N:
        pipo.append(pipo[-1]+pipo[-2])
    print(pipo[-1]+pipo[-2])