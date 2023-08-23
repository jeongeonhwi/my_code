import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    secret_code = []
    for _ in range(N):
        arr = list(input().strip())
        a = arr.count('1')
        if a != 0:
            secret_code.append(arr)
    code = []
    for i in range(len(secret_code)):
        idx = 0
        for j in range(len(secret_code[i])-1, -1, -1):
            if secret_code[i][j] == '1':
                idx = j
                break
        code.append(secret_code[i][idx-55:idx+1])
    num_list = []
    for i in range(len(code)):
        num = []
        for j in range(0, len(code[i]), 7):
            if code[i][j] == '0' and code[i][j+1] == '0' and code[i][j+2] == '0' and code[i][j+3] == '1' and code[i][j+4] == '1' and code[i][j+5] == '0' and code[i][j+6] == '1':
                num.append(0)
            elif code[i][j] == '0' and code[i][j+1] == '0' and code[i][j+2] == '1' and code[i][j+3] == '1' and code[i][j+4] == '0' and code[i][j+5] == '0' and code[i][j+6] == '1':
                num.append(1)
            elif code[i][j] == '0' and code[i][j+1] == '0' and code[i][j+2] == '1' and code[i][j+3] == '0' and code[i][j+4] == '0' and code[i][j+5] == '1' and code[i][j+6] == '1':
                num.append(2)
            elif code[i][j] == '0' and code[i][j+1] == '1' and code[i][j+2] == '1' and code[i][j+3] == '1' and code[i][j+4] == '1' and code[i][j+5] == '0' and code[i][j+6] == '1':
                num.append(3)
            elif code[i][j] == '0' and code[i][j+1] == '1' and code[i][j+2] == '0' and code[i][j+3] == '0' and code[i][j+4] == '0' and code[i][j+5] == '1' and code[i][j+6] == '1':
                num.append(4)
            elif code[i][j] == '0' and code[i][j+1] == '1' and code[i][j+2] == '1' and code[i][j+3] == '0' and code[i][j+4] == '0' and code[i][j+5] == '0' and code[i][j+6] == '1':
                num.append(5)
            elif code[i][j] == '0' and code[i][j+1] == '1' and code[i][j+2] == '0' and code[i][j+3] == '1' and code[i][j+4] == '1' and code[i][j+5] == '1' and code[i][j+6] == '1':
                num.append(6)
            elif code[i][j] == '0' and code[i][j+1] == '1' and code[i][j+2] == '1' and code[i][j+3] == '1' and code[i][j+4] == '0' and code[i][j+5] == '1' and code[i][j+6] == '1':
                num.append(7)
            elif code[i][j] == '0' and code[i][j+1] == '1' and code[i][j+2] == '1' and code[i][j+3] == '0' and code[i][j+4] == '1' and code[i][j+5] == '1' and code[i][j+6] == '1':
                num.append(8)
            elif code[i][j] == '0' and code[i][j+1] == '0' and code[i][j+2] == '0' and code[i][j+3] == '1' and code[i][j+4] == '0' and code[i][j+5] == '1' and code[i][j+6] == '1':
                num.append(9)
        num_list.append(num)
    even = 0
    ord = 0
    for i in range(4):
        even += num_list[0][i*2]
        ord += num_list[0][i*2+1]
    even *= 3

    if (ord+even)%10 == 0:
        print(f'#{tc} {even//3 + ord}')
    else:
        print(f'#{tc} 0')