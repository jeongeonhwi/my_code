from book import decrease_book

number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    user_info = {
        'name': name,
        'age': age,
        'address': address
    }
    print(f'{name}님 환영합니다.')
    increase_user()

    return user_info


many_user = list(map(create_user, name, age, address))


def rental_book(info):
    num = info['age'] // 10
    decrease_book(num)
    print(f'{info["name"]}님이 {num}권의 책을 대여하였습니다.')


info_user = map(lambda user: {'name': user['name'], 'age': user['age']}, many_user)

list(map(rental_book, info_user))