import sys
sys.stdin = open('input.txt', 'r')
# 1은 북, 2는 남, 3은 서 4는 동
w, h = map(int, input().split())
store = int(input())
count = 0
slist = []
for _ in range(store):
    way, po = map(int, input().split())
    slist.append(way)
    slist.append(po)
dway, dpo = map(int, input().split())
if dway == 1:
    for i in range(store):
        if dway == slist[i*2]:
            count += abs(dpo-slist[i*2+1])
        elif slist[i*2] == 2:
            if slist[i*2+1]+h+dpo < (w*2+h*2)-(slist[i*2+1]+h+dpo):
                count += slist[i*2+1]+h+dpo
            else:
                count += (w*2+h*2)-(slist[i*2+1]+h+dpo)
        elif slist[i*2] == 3:
            count += dpo+slist[i*2+1]
        elif slist[i*2] == 4:
            count += slist[i*2+1]+w-dpo
elif dway == 2:
    for i in range(store):
        if dway == slist[i*2]:
            count += abs(dpo-slist[i*2+1])
        elif slist[i*2] == 1:
            if slist[i*2+1]+h+dpo < (w*2+h*2)-(slist[i*2+1]+h+dpo):
                count += slist[i*2+1]+h+dpo
            else:
                count += (w*2+h*2)-(slist[i*2+1]+h+dpo)
        elif slist[i*2] == 3:
            count += dpo+h-slist[i*2+1]
        elif slist[i*2] == 4:
            count += h-slist[i*2+1]+w-dpo
elif dway == 3:
    for i in range(store):
        if dway == slist[i*2]:
            count += abs(dpo-slist[i*2+1])
        elif slist[i*2] == 4:
            if slist[i*2+1]+w+dpo < (w*2+h*2)-(slist[i*2+1]+w+dpo):
                count += slist[i*2+1]+w+dpo
            else:
                count += (w*2+h*2)-(slist[i*2+1]+w+dpo)
        elif slist[i*2] == 1:
            count += dpo+slist[i*2+1]
        elif slist[i*2] == 2:
            count += slist[i*2+1]+h-dpo
elif dway == 4:
    for i in range(store):
        if dway == slist[i*2]:
            count += abs(dpo-slist[i*2+1])
        elif slist[i*2] == 3:
            if slist[i*2+1]+w+dpo < (w*2+h*2)-(slist[i*2+1]+w+dpo):
                count += slist[i*2+1]+w+dpo
            else:
                count += (w*2+h*2)-(slist[i*2+1]+w+dpo)
        elif slist[i*2] == 1:
            count += dpo+w-slist[i*2+1]
        elif slist[i*2] == 2:
            count += w-slist[i*2+1]+h-dpo
print(count)