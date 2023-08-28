# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(my_list):
    # pop과 extend 를 활용하여 홀수를 제거하자!
    # pop 데이터를 빼는 것
    # extend는 추가하는 것
    new_list = []
    while len(my_list):
        my_num = my_list.pop(0)  # 값을 빼고
        if my_num % 2 == 0:  # 짝수면
            new_list.extend([my_num]) # 리스트에 추가한다.
    return new_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)