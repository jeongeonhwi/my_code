N = int(input())

card = [i for i in range(1, N+1)]

if len(card) == 1:
    print(*card)
elif len(card) == 2:
    print(card[1])
else:
    while True:
        tmp = []
        for i in range(len(card)):
            if i%2==0:
                continue
            tmp.append(card[i])
        if len(card)%2 == 1:
            tmp = [card[-1]] + tmp
        if len(tmp) == 2:
            print(tmp[1])
            break
        elif len(tmp) == 1:
            print(*tmp)
            break
        else:
            card = tmp