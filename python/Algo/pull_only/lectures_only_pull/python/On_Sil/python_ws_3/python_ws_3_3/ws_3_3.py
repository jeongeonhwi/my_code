from book import decrease_book

# ws_3_3.py
def rental_book(name, num):
    decrease_book(num)
    print(f'{name}님이 {num}권의 책을 대여하였습니다.')


rental_book('홍길동', 3)