'''
탐욕 알고리즘 적용 문제

'''
N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]

meeting = []
for i in range(N):
    meeting.append([a[i*2], a[i*2+1]])
meeting.sort(key=lambda x:x[1])
meeting = [[0,0]]+meeting

s = []
j = 0
for i in range(1, N+1):
    if meeting[i][0] >= meeting[j][1]:  # si>=fj
        s.append(i)
        j = i
print(s)