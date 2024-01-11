# 프로젝트 만들기
## 프로젝트 4까지
### 장고로 그래프 만드는 방법
```python
# matplotlib, numpy, pandas 설치하고
import matplotlib.pyplot as plt

# 예제1: x,y 가 같을 때
plt.plot([1,2,3,4])
# plt.show()

# 참고: 이때까지 그렸던 plot 지우기
plt.clf()

# 예제2: x, y가 다를때
x = [1,2,3,4]
y = [2,4,8,16]

# plt.plot(x,y)
# plt.show()

# 예제3: 제목 + 각 축의 설명
plt.plot(x,y)
# 제목
# 한글을 쓰면 깨진다. 추가적인 설정이 필요함. 구글링 요망
plt.title("Test Graph")

# x, y 축
plt.ylabel('y label')
plt.xlabel('x label')

# plt.show()

# 파일로 저장하기
# 주의사항: show()를 하지 말고 저장해야 한다.
plt.savefig('filename.png')
```
### 웹 페이지에 그래프 출력하기
```python
import matplotlib.pyplot as plt

# io: 입출력 연산을 위한 python 표준 라이브러리
# BytesIO: 이진 데이터를 다루기 위한 버퍼를 제공
# 버퍼: 임시 저장 공간
# 파일 시스템과 유사하지만, 
# 실제로 파일로 만들지 않고 메모리 단에서 작업할 수 있음
from io import BytesIO

# 텍스트와 이진데이터를 변환할 수 있는 모듈
import base64

# 참고. 터미널 에러
# UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail.
# plt를 만드는 곳과 화면에 그리는 곳이 달라서 오류가 날 수 있다. 경고를 준다!
# 백엔드를 agg로 설정하여 해결
plt.switch_backend('Agg')


# 그래프를 그려보자
def index(request):

    x = [1,2,3,4]
    y = [2,4,8,16]

    # 다른 view 함수에서 plt 를 이미 그린 상태에서
    # 다시 그리는 경우를 대비하여, 초기화를 진행
    plt.clf()

    plt.plot(x,y)
    plt.title("Graph")
    plt.ylabel('y label')
    plt.xlabel('x label')

    # 비어있는 버퍼를 생성
    buffer = BytesIO()

    # 버퍼에 ㅡ래프를 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')

    # 버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹 페이지에 표시하기 위해
    # URI 형식(주소 형식)으로 만들어진 문자열을 생성
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'myapp/index.html', context)
```
### account 앱을 만들어서 유저 커스텀 하기
```python
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Django 가 기본적으로 user 모델을
# 왜 덮어써야 하는가?
# 1. Django 권장사항
# 2. 커스텀을 하기 위해서
class User(AbstractUser):
    # 내가 원하는 추가적인 필드를 사용
    nickname = models.CharField(max_length=30)
# 꼭 추가 필드 설정해보기
```
### 그린 그래프표를 화면에 띄우기
```python
# app/views.py
import pandas as pd
csv_path = 'myapp/data/austin_weather.csv'


def example(request):
    df = pd.read_csv(csv_path)
    context = {
        'df':df,
    }
    return render(request, 'myapp/example.html', context)
```
```html
  <h1>Pandas 써보기</h1>
  <table>
    <tr>
      {% for column in df.columns %}
        <th>
          {{ column }}
        </th>
      {% endfor %}
    </tr>
    {% for row in df.values %}
      <tr>
        {% for value in row %}
          <td>
            {{ value }}
          </td>
        {% endfor %}
      </tr>
    {% endfor %}
  </table>
```
## 프로젝트
