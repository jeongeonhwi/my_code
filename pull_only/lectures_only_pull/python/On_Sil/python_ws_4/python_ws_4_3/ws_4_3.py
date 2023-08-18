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

print(dummy_data)