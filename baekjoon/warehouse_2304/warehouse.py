import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [0]*1002
llist = []
for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H
    llist.append(L)
llist.sort()
# arr = []
# if len(llist) > 1:
#     for i in range(llist[-1]+2):
#         arr.append(arr2[i])

max_v = 0
max_idx = 0
max_count = 0
max_min_idx = 0
for i in range(len(arr)):
    if arr[i] >= max_v:
        max_v = arr[i]
        max_idx = i
for i in range(len(arr)):
    if max_v == arr[i]:
        max_count += 1

if max_count > 1:
    for i in range(len(arr)):
        if arr[i] == max_v:
            max_min_idx = i
            break


total = 0
current_v = 0
current_idx = 0

if len(llist) > 1:
    for i in range(len(arr)):
        if current_v == 0 and arr[i] != 0 and arr[i] != max_v:
            current_v = arr[i]
            current_idx = i
        elif arr[i] != max_v and current_v < arr[i]:
            total += current_v*(i-current_idx)
            current_v = arr[i]
            current_idx = i
        elif arr[i] == max_v:
            total += current_v*(i-current_idx)
            current_v = 0
            current_idx = 0
            break

    for i in range(len(arr)-1, -1, -1):
        if current_v == 0 and arr[i] != 0 and arr[i] != max_v:
            current_v = arr[i]
            current_idx = i
        elif arr[i] != max_v and current_v < arr[i]:
            total += current_v * (current_idx - i)
            current_v = arr[i]
            current_idx = i
        elif arr[i] == max_v:
            total += current_v * (current_idx - i)
            current_v = 0
            current_idx = 0
            break
    if max_count == 1:
        total += max_v
    elif max_count > 1:
        total += max_v*(max_idx+1-max_min_idx)
elif len(llist) == 1:
    total = arr[llist[0]]

print(total)