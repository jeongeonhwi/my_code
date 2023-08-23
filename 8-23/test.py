import sys
# input 파일을 읽어오는 함수
sys.stdin = open("input.txt","r")
# output 파일로 프린트값을 보내줌
sys.stdout = open("output.txt", "w")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(N, arr)