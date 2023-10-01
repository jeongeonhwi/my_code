import copy

def a(arr):
    arr2 = copy.deepcopy(arr)
    arr2[0][0] = 100
    return arr2


arr = [[0,0],[1,2]]
r = a(arr)
arr = r
print(arr)