import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())
st_j, st_i = map(int, input().split())
t = int(input())
total_i = h
total_j = w
time_i = t%(total_i*2)
time_j = t%(total_j*2)
i = time_i+st_i
j = time_j+st_j
result = []
if i == total_i:
    result.append(i)
elif i < total_i:
    result.append(i)
elif i > total_i and i <= 2*total_i:
    result.append(total_i-(i-total_i))
elif i > 2*total_i:
    result.append(i-total_i*2)

if j == total_j:
    result.append(j)
elif j < total_j:
    result.append(j)
elif j > total_j and j <= 2*total_j:
    result.append(total_j-(j-total_j))
elif j > 2*total_j:
    result.append(j-total_j*2)
result.reverse()
print(*result)