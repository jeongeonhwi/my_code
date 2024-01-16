# def find_set(x):
#     if parents[x] == x:
#         return x
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
#
# def union(x,y):
#     x = find_set(x)
#     y = find_set(y)
#     if x == y:
#         return
#     if x < y:
#         parents[y] = x
#     else:
#         parents[x] = y


def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
