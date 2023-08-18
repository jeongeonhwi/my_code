import requests
from pprint import pprint as print

dummy_data = []
for user_number in range(1, 11):
    dummy_dict = {}
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{user_number}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    lat = float(parsed_data.get('address').get('geo').get('lat'))
    lng = float(parsed_data.get('address').get('geo').get('lng'))

    if (-80 < lat < 80) and (-80 < lng < 80):
        dummy_dict['name'] = parsed_data.get('name')
        dummy_dict['lat'] = lat
        dummy_dict['lng'] = lng
        dummy_dict['company_name'] = parsed_data.get('company').get('name')

        dummy_data.append(dummy_dict)

BLACK_LIST = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']


def censorship(user_data):
    company = user_data.get('company_name')
    name = user_data.get('name')
    if company in BLACK_LIST:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True


def create_user(dummy_data):
    censored_user_dict = {}
    for data in dummy_data:
        result = censorship(data)
        # censored_user_dict[data.get('company')] = [data.get('name')]
        if result:
            if censored_user_dict.get(data.get('company_name')):
                # 값이 있으면 리스트에 append
                censored_user_dict[data.get('company_name')].append(data.get('name'))
            else:
                censored_user_dict[data.get('company_name')] = [data.get('name')]
    
    return censored_user_dict

        
res = create_user(dummy_data)
print(res)