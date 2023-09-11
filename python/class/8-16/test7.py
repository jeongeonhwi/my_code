#거듭제곱
def f1(b, e):
    global count1

    if b == 0:
        return 1
    r = 1
    for i in range(e):
        r*=b
        count1 += 1
    return r

def f2(b, e):
    global count2

    if b ==0 or e == 0:
        return 1
    #홀수면
    if e%2:
        r = f2(b, (e-1)//b)
        count2 += 1
        return r*r*b
    #짝수면
    else:
        r = f2(b, e//b)
        count2 += 1
        return r*r

count1 = 0
count2 = 0

print(f1(2, 10), count1)
print(f2(2, 10), count2)