arr = [[[] for _ in range(3)] for _ in range(3)]
arr[0][0].append(3)
tmp = []
while arr[0][0]:
    i = arr[0][0].pop()
    if groud[0][0] < i:
        continue
