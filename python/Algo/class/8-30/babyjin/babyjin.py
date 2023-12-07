import sys
sys.stdin = open('input.txt', 'r')

def card_win(player1, player2, arr):
    for i in range(6):
        player1.append(arr[i*2])
        count = 1
        if len(player1) >=3:
            player1.sort()
            # print(player1)
            for j in range(len(player1)-1):
                if player1[j]+1 == player1[j+1]:
                    count += 1
                    if count >= 3:
                        return 1
                elif player1[j] != player1[j+1]:
                    count = 1
            for j in player1:
                if player1.count(j) >= 3:
                    return 1
        player2.append(arr[i * 2 + 1])
        count2 = 1
        if len(player2) >=3:
            player2.sort()
            for j in range(len(player2)-1):
                if player2[j]+1 == player2[j+1]:
                    count2 += 1
                    if count2 >= 3:
                        return 2
                elif player2[j] != player2[j+1]:
                    count2 = 1
            for j in player2:
                if player2.count(j) >= 3:
                    return 2
    return 0


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player1 = []
    player2 = []
    ans = card_win(player1, player2, arr)
    print(f'#{tc} {ans}')