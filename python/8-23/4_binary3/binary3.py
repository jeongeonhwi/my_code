import sys
sys.stdin = open('input.txt', 'r')

sixteen_dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,
            '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
            '8':8,'9':9}
T = int(input())
for tc in range(1, T+1):
    N, s = list(input().split())
    b_list = [0] * int(N)*4
    count = 0
    for i in range(int(N)):
        count += sixteen_dict[s[i]]*16**(int(N)-1-i)
    idx = 0
    # while True:
    #     if count < 2**idx:
    #         break
    #     idx += 1
    while True:
        if count == 0:
            break
        if count >= 2**(len(b_list)-1-idx):
            b_list[idx] = 1
            count -= 2**(len(b_list)-1-idx)
        idx += 1
    print(f'#{tc} ', end='')
    for i in b_list:
        print(i, end='')
    print()