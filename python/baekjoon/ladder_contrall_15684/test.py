def combi(s,k,e):
    if s == e:
        print(com)
        return
    for i in range(k,N):
        com[s] = arr[i]
        combi(s+1,i+1,e)


arr = [1,2,3,4,5,6,7,8,9,10]
N = 10
e = 3
com = [0]*e
combi(0,0,e)
#
#

# arr = [j for j in range(1, 6)]
# sets = [0] * 3
# N = len(arr)
# def combi(s, k, e):
#     if s == e:
#         print(sets)
#     else:
#         for i in range(k, N):
#             sets[s] = arr[i]
#             combi(s+1, i+1, e)
# combi(0, 0, 3)