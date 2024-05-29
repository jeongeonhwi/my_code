while True:
    data = list(map(str, input().split()))
    data[1], data[2] = int(data[1]), int(data[2])
    if data[0] == 0 and data[1] == 0:
        break
    if data[1] > 17 or data[2] >= 80:
        print(data[0], "Senior")
    else:
        print(data[0], "Junior")