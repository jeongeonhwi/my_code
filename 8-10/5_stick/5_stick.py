import sys
sys.stdin= open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input()))
    laser = []
    stick = []
    openlist = []
    closelist = []
    sticklist = []
    open1 = '('
    close1 = ')'
    #레이저 리스트에 넣기
    for i in range(len(arr)-1):
        if arr[i] == open1 and arr[i+1] == close1:
            laser.append(i)
            laser.append(i+1)
    # print(laser)
    # 오픈 인덱스 리스트에 넣기
    for i in range(len(arr)):
        if i not in laser and arr[i] == open1:
            openlist.append(i)
    # print(openlist)
    # 클로즈 인덱스 리스트에 넣기
    for i in range(len(arr)):
        if i not in laser and arr[i] == close1:
            closelist.append(i)
    # print(closelist)

    if laser[0] < openlist[0]:
        laser.pop(0)
        laser.pop(0)
    if laser[-1] > closelist[-1]:
        laser.pop(-1)
        laser.pop(-1)
    # print(laser)
    # 쇠막대기 인덱스값 리스트에 넣기
    # for i in range(len(closelist)):
    #     #맥스리스트 만들기
    #     maxlist = []
    #     max_v = 0
    #     for j in range(len(openlist)):
    #         if openlist[j] < closelist[i]:
    #             maxlist.append(openlist[j])
    #     for k in range(len(maxlist)):
    #         if max_v < maxlist[k]:
    #             max_v = maxlist[k]
    #     openlist.pop(len(maxlist)-1)
    #     sticklist.append(max_v)
    #     sticklist.append(closelist[i])
    # print(sticklist)

    # 쇠막대기 인덱스값 리스트에 넣기2222

    for i in range(len(laser)//2):
        if len(openlist) != 0 or len(closelist) != 0:
            if laser[i*2] - laser[i*2-1] != 1:
                tem = []
                max_v = 0
                maxidx = 0
                for j in range(len(openlist)):
                    if laser[i*2] > openlist[j]:
                        tem.append(openlist[j])
                for j in range(len(tem)):
                    if max_v < tem[j]:
                        max_v = tem[j]
                        maxidx = j

                openlist.pop(maxidx)
                sticklist.append(max_v)

                tem = []
                min_v = closelist[-1]
                minidx = 0
                for j in range(len(closelist)):
                    if laser[i * 2 +1] < closelist[j]:
                        tem.append(closelist[j])
                for j in range(len(tem)):
                    if min_v > tem[j]:
                        min_v = tem[j]
                        minidx = j

                closelist.pop(minidx)
                sticklist.append(min_v)
    # sticklist.append(openlist[0])
    # sticklist.append(closelist[0])
    # print(openlist)
    # print(closelist)
    # print(sticklist)

    result = 0
    for i in range(len(sticklist)//2):
        checklist = []
        count = 0
        for j in range(sticklist[i*2], sticklist[i*2+1]+1):
            checklist.append(j)
        for k in range(len(laser)//2):
            if laser[k*2] in checklist:
                count += 1
        result += (count + 1)

    print(f'#{tc} {result}')
