# book.py
number_of_book = 100

def decrease_book(num):
    global number_of_book
    number_of_book -= num
    print(f'현재 남은 책의 수 : {number_of_book}')