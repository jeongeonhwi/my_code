n = 2
data = [[1,2,3,4,5],[6,7,8],[9,10]]

def func(depth, n, save_tmp):
    if depth == n:
        print(save_tmp)
        return
    for x in data[depth]:
        save_tmp.append(x)
        func(depth+1, n, save_tmp)
        save_tmp.pop()


func(0, n, [])