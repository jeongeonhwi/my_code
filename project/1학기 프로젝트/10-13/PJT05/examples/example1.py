import requests
from bs4 import BeautifulSoup

def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    response = requests.get(url)
    # 우리가 얻고자 하는 HTML 내용이 여기 담깁니다.
    html_text = response.text

    # html 을 파싱이 가능한 정리된 형태로 변환
    soup = BeautifulSoup(html_text, 'html.parser')

    
    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())


get_google_data('파이썬')