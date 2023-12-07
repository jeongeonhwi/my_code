import sys
sys.stdin = open("input.txt")

# T = int(input())
# for tc in range(1, T+1):
#     num, N = map(str, input().split())
#     arr = list(map(str, input().split()))
#     sortedlist = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#     for i in range(len(arr), 0, -1):
#         for j in range(1, i):
#             sidx = 0
#             ssidx = 0
#             for k in range(len(sortedlist)):
#                 if arr[j] == sortedlist[k]:
#                     sidx = k
#                 if arr[j-1] == sortedlist[k]:
#                     ssidx = k
#             if sidx < ssidx:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#     print(num)
#     for k in range(len(arr)):
#         print(arr[k], end=" ")
#     print()

T = int(input())
for tc in range(1, T+1):
    num, N = map(str, input().split())
    arr = list(map(str, input().split()))
    # sortedlist = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    zrolist = []
    onelist = []
    twolist = []
    thrlist = []
    forlist = []
    fivlist = []
    sixlist = []
    svnlist = []
    egtlist = []
    ninlist = []
    for i in range(len(arr)):
        if arr[i] == 'ZRO':
            zrolist.append(arr[i])
        elif arr[i] == 'ONE':
            onelist.append(arr[i])
        elif arr[i] == 'TWO':
            twolist.append(arr[i])
        elif arr[i] == 'THR':
            thrlist.append(arr[i])
        elif arr[i] == 'FOR':
            forlist.append(arr[i])
        elif arr[i] == 'FIV':
            fivlist.append(arr[i])
        elif arr[i] == 'SIX':
            sixlist.append(arr[i])
        elif arr[i] == 'SVN':
            svnlist.append(arr[i])
        elif arr[i] == 'EGT':
            egtlist.append(arr[i])
        elif arr[i] == 'NIN':
            ninlist.append(arr[i])

    zrolist.extend(onelist)
    zrolist.extend(twolist)
    zrolist.extend(thrlist)
    zrolist.extend(forlist)
    zrolist.extend(fivlist)
    zrolist.extend(sixlist)
    zrolist.extend(svnlist)
    zrolist.extend(egtlist)
    zrolist.extend(ninlist)
    # print(zrolist)
    print(num)
    for k in zrolist:
        print(k, end=" ")
    print()
