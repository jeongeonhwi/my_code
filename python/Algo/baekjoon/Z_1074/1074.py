import sys
sys.stdin = open('input.txt', 'r')


N, r, c = map(int, input().split())

gi,gj = r, c
nsi,nei = 0, 2**N-1
nsj,nej = 0, 2**N-1
cnt = 0
# check = 0
while True:
    # check += 1
    # if check >= 3:
    #     break
    if (nei-nsi+1)*(nej-nsj+1) == 4:
        if nsi == gi and nsj == gj:
            print(cnt)
        elif nsi == gi and nej == gj:
            print(cnt+1)
        elif nej == gi and nsj == gj:
            print(cnt+2)
        else:
            print(cnt+3)
        break
    if nsi+(nei-nsi+1)//2 <= gi and nsj+(nej-nsj+1)//2 <= gj:
        cnt += ((nei-nsi+1)//2)*((nej-nsj+1)//2)*3
        # nsi,nsj = (nei-nsi+1)//2,(nej-nsj+1)//2
        nsi += (nei-nsi+1)//2
        nsj += (nej-nsj+1)//2
    elif nsi+(nei-nsi+1)//2 <= gi and nsj+(nej-nsj+1)//2 > gj:
        cnt += ((nei - nsi + 1) // 2) * ((nej - nsj + 1) // 2) * 2
        # nsi,nej = (nei-nsi+1)//2,(nej-nsj+1)//2-1
        nsi += (nei-nsi+1)//2
        nej = nsj + (nej-nsj+1)//2-1
    elif nsi+(nei-nsi+1)//2 > gi and nsj+(nej-nsj+1)//2 <= gj:
        cnt += ((nei - nsi + 1) // 2) * ((nej - nsj + 1) // 2) * 1
        # nei,nsj = (nei-nsi+1)//2-1,(nej-nsj+1)//2
        nei = nsi + (nei-nsi+1)//2-1
        nsj += (nej - nsj + 1) // 2
    elif nsi+(nei-nsi+1)//2 > gi and nsj+(nej-nsj+1)//2 > gj:
        # nei,nej = (nei-nsi+1)//2-1,(nej-nsj+1)//2-1\
        nei = nsi + (nei - nsi + 1) // 2 - 1
        nej = nsj + (nej - nsj + 1) // 2 - 1
    # print(nsi,nei)
    # print(nsj,nej)
    # print((nei-nsi+1)*(nej-nsj+1))
    # print(cnt)
