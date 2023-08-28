import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
student = []
result = []
for i in range(1, N+1):
    student.append(i)
# print(student)
for i in range(N):
    result.insert(i-arr[i], student[i])
    # print(result)
print(*result)