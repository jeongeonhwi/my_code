import sys
sys.stdin = open('input.txt', 'r')
# 첫째줄은 정식이가 기억하는 송금액의 2진수, 두번째줄은 송금액의 3진수

def find_money(bin, three):
    for i in range(1, len(bin)):
        if bin[i] == '1':
            bin[i] = '0'
        else:
            bin[i] = '1'
        for j in range(len(three)):
            for k in range(3):
                if j == 0 and k == 0:
                    pass
                else:
                    if three[j] != str(k):
                        tmp = three[j]
                        three[j] = str(k)
                        b = ''.join(bin)
                        t = ''.join(three)
                        if int(b, 2) == int(t, 3):
                            result = int(b, 2)
                            return result
                        else:
                            three[j] = tmp
        if bin[i] == '1':
            bin[i] = '0'
        else:
            bin[i] = '1'



T = int(input())
for tc in range(1, T+1):
    bin = list(input())
    three = list(input())
    ans = find_money(bin, three)
    print(f'#{tc} {ans}')