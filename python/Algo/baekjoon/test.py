a = [(1,(1,1)), (2,(2,2))]
from heapq import heappop, heappush

heappush(a, (3,(3,3)))
print(a)