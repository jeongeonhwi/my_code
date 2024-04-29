import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
import copy

# 태연의 선호도 6,7,8,9,10
T = int(input())
for _ in range(T):
    meeting = [[],[6,7,8,9,10]]
    for _ in range(9):
        data = list(map(int, input().split()))
        meeting.append(data)
    for i in range(1, 6):
        meeting[i].append(0)
    for i in range(6,11):
        meeting[i].append(False)
    first_meeting = copy.deepcopy(meeting)
    while True:
        for i in range(6,11):
            if not first_meeting[i][-1]:
                # 여학생의 선호 남학생
                for j in first_meeting[i][:5]:
                    # 남학생의 커플이 0이면
                    if first_meeting[j][-1] == 0:
                        first_meeting[j][-1] = i
                        break
                    else:
                        # 남학생의 커플이 존재하면
                        for mj in first_meeting[j]:
                            if mj == first_meeting[j][-1]:
                                break
                            elif i == mj:
                                bgirl = first_meeting[j][-1]
                                first_meeting[j][-1] = i
                                first_meeting[i][-1] = True
                                # 이거 미팅 저장해야지 안그러면 실시간 여학생 짝 위치가 바뀜
                                first_meeting[bgirl] = False