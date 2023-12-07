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
    # sticklist2 = []
    open1 = '('
    close1 = ')'
    #레이저 리스트에 넣기          오름차순
    for i in range(len(arr)-1):
        if arr[i] == open1 and arr[i+1] == close1:
            laser.append(i)
            laser.append(i+1)
    # print(laser)
    # 오픈 인덱스 리스트에 넣기      오름차순
    for i in range(len(arr)):
        if i not in laser and arr[i] == open1:
            openlist.append(i)
    print(openlist)
    # 클로즈 인덱스 리스트에 넣기     오름차순
    for i in range(len(arr)):
        if i not in laser and arr[i] == close1:
            closelist.append(i)
    print(closelist)

    # 사용못하는 쓸모없는 레이저 요소 제거
    trash = []
    for i in range(len(laser)//2-1):
        if laser[i*2] - laser[i*2 + 2] == -2:
            trash.append(laser[i*2+1])
            trash.append(laser[i*2+2])
    # print(trash)
    laser2 = []
    for i in range(len(laser)):
        if laser[i] not in trash:
            laser2.append(laser[i])
    print(laser2)
    max_v = 0
    if max_v < laser[-1]:
        max_v = laser[-1]
    if max_v < openlist[-1]:
        max_v = openlist[-1]
    if max_v < closelist[-1]:
        max_v = closelist[-1]

    opencount = [0]*(max_v+1)
    closecount = [0]*(max_v+1)
    laser2count = [0]*(max_v+1)

    for i in range(len(openlist)):
        opencount[openlist[i]] = 1
    for i in range(len(closelist)):
        closecount[closelist[i]] = 1
    for i in range(len(laser2)):
        laser2count[laser2[i]] = 1

    # for i in range(len(laser2count)):


    # print(opencount)
    # print(closecount)
    # print(laser2count)
    openpoint = 0
    laserpoint = 0
    for i in range(len(laser2count)):
        if opencount[i] == 1:
            openpoint = i
        if openpoint != 0:
            if i +2 < len(laser2count):
                if laser2count[i] == 1:
                    laserpoint += 1
                    if laserpoint % 2 == 1:
                        sticklist.append(openpoint)
                        opencount[openpoint] = 0
                        for j in range(i, len(laser2count)):
                            if closecount[j] == 1:
                                # closepoint = j
                                sticklist.append(j)
                                closecount[j] = 0
                                break
    openlist2 = []
    closelist2 = []
    for i in range(len(openlist)):
        if openlist[i] == 1:
            openlist2.append(i)
        if closelist[len(openlist)-1-i] == 1:
            closelist2.append(len(openlist)-1-i)
    if len(closelist2) > len(openlist2):
        for i in range(len(openlist2)):
            sticklist.append(openlist2[i])
            sticklist.append(closelist2[i])
    else:
        for i in range(len(closelist2)):
            sticklist.append(openlist2[i])
            sticklist.append(closelist2[i])
    print(opencount)
    print(closecount)
    print(sticklist)



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
