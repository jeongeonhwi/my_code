import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
if N == 0:
    print(0)
else:
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()
    arr = deque(arr)
    except_data = N/100*15
    if except_data >= int(except_data)+0.5:
        except_data = int(except_data)+1
    else:
        except_data = int(except_data)
    for _ in range(except_data):
        arr.pop()
        arr.popleft()
    ans = sum(arr)/len(arr)
    if ans >= int(ans)+0.5:
        print(int(ans)+1)
    else:
        print(int(ans))