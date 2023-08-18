#교수님 써머리 시작 부분집합 재귀사용 백트래킹사용

#부분집합
arr = list(range(1, 11))
# 해당 숫자가 선택됐는지 안됐는지 확인 용도
selected = [False]*(len(arr)+1)

#idx는 현재 숫자, 위치
def powerset(idx):

    # 종료 조건을 만들자!!
    if idx == len(arr)+1:    # +1을 붙인 이유 => selected 크기가 len(arr)+1 이기 때문
        # 종료 전에 현재 선택된 부분집합을 출력
        for i in range(len(arr)+1):
            if selected[i] == True:
                print(i, end=' ')
        print()               # 줄바꿈 용도
        return                #함수 종료(break를 사용하듯이 함수를 종료하지 위한 목적)

    # 현 위치를 선택했을 경우
    selected[idx] = True
    powerset(idx+1)  # 다음자리 선택

    # 현 위치를 선택하지 않을 경우
    selected[idx] = False
    powerset(idx+1)  # 다음자리 선택

powerset(1)  #시작이 1인 이유 : 0번 index를 selected에서 사용하지 않기 때문