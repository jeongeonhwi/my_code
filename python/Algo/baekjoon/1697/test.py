from collections import deque

a = [1, 2, 3]
tmp = deque(a)
print(tmp.popleft())
print(tmp)