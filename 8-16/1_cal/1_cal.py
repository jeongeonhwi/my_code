import sys
sys.stdin = open('input.txt')

isp = {'+':1, '-':1, '/':2, '*':2}
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = input()
    s = ''
    stack1 = [0]*(len(arr)+1)
    top1 = -1
    for i in arr:
        #숫자들 모으기
        if i not in '+-/*':
            s += i
        else:
            #수식들 조건추가해서 모으기
            if stack1[top1] == 0 or isp[stack1[top1]] <= isp[i]:
                top1 += 1
                stack1[top1] = i
            else:
                while top1 > -1 and isp[stack1[top1]] > isp[i]:
                    s += stack1[top1]
                    top1 -= 1
                # 본인보다 순위높은 부호들을 털어내고 그 다음 수식 추가해주기
                top1 += 1
                stack1[top1] = i
    #stack에 남아있는 수식들 털기
    while top1 > -1:
        s += stack1[top1]
        top1 -= 1
    #s에 모인 숫자와 수식들 후위표기식 계산해주기
    stack2 = [0]*(len(arr)+1)
    top2 = -1
    for i in s:
        if i not in '+-/*':
            top2 += 1
            stack2[top2] = int(i)
        else:
            op2 = stack2[top2]
            top2 -= 1
            op1 = stack2[top2]
            top2 -= 1

            if i == '+':
                a = op1 + op2
                top2 += 1
                stack2[top2] = a
            elif i == '*':
                a = op1 * op2
                top2 += 1
                stack2[top2] = a
    print(f'#{tc} {stack2[top2]}')
