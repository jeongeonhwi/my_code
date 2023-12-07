def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    l_arr, e_arr, h_arr = [], [], []
    for i in arr:
        if i < pivot:
            l_arr.append(i)
        elif i > pivot:
            h_arr.append(i)
        else:
            e_arr.append(i)
    return quicksort(l_arr) + e_arr + quicksort(h_arr)

a = [3, 2, 1, 3, 2, 1, 3, 2, 1]

print(quicksort(a))
print(a)