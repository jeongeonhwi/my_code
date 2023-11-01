n = 'bbbbbaaaaaabbbbb'
ncnt = len(n)
for i in range(ncnt):
    bcheck = False
    if N[i] == 'b':
        for j in range(bcnt):
            if N[(i + j) % ncnt] != 'b':
                bcheck = True
                break
        else:
            min_v = min(min_v, c)
            return
    if bcheck:
        break