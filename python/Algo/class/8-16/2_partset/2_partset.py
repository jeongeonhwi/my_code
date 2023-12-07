import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))
select = [False] *(len(arr)+1)
count = 0
def f(idx):
    if idx == len(arr)+1:
        s = 0
        for i in range(len(arr)+1):
            if select[i] == True:
                s += i
        if s == 10:
            global count
            count += 1
        return

    select[idx] = True
    f(idx+1)
    select[idx] = False
    f(idx+1)
f(1)
print(f'#1 {count}')