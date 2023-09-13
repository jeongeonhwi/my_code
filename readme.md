# Django
-----
### django
python 기반의 대표적인 웹 프레임워크
### 웹의 동작 방식
client가 server에 요청
server가 client에 응답
### Client
서비스를 요청하는 주체(웹 사용자의 인터넷이 연결된 장치, 웹 브라우저)
### Server
클라이언트의 요청에 응답하는 주체(웹 페이지, 앱을 저장하는 컴퓨터)
### 가상환경
Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행 환경
### 가상환경 venv 생성
깃베쉬 켜기  
python -m venv venv  
여기까지 명령어/이 뒤가 가상환경 이름
### 가상환경 활성화
이동의 개념이 아니라 온/오프 개념 깃베쉬로 해당 가상환경을 켜는것  
source venv/Scripts/activate
### 가상환경 비활성화
deactivate  
가상환경을 오프하는 명령어  
깃베쉬를 꺼도 오프된다.
### 설치된 패키지 확인
pip list
### 공동으로 프로젝트를 진행할 경우 설치된 패키지와 버전을 공유
pip freeze  
pip freeze > requirements.txt  
(가상환경의 용량이 너무 크기때문에 txt파일을 보냄)
### 공유받은 패키지 텍스트 파일을 한번에 설치하는법
python -m venv venv (가상환경 생성)  
source venv/Scripts/activate  
pip list  
pip install -r requirements.txt  (미리 공유받은 텍스트파일 저장해놓기)  
pip list  
### 의존성 패키지
한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계  
사용하려는 패키지가 설치되지 않았거나, 호환되는 버전이 아니면 오류가 발생하거나 예상치 못한 동작을 보일 수 있음
### Django 프로젝트 생성 전 루틴
1. python -m venv venv  
2. source venv/Scripts/activate  
3. pip install django
4. pip freeze > requirements.txt  (새로운 패키지 다운받았으므로 requirements 업데이트)
### Django 프로젝트 생성
django-admin startproject firstpjt .  
--------여기까지가 명령어 / 여기는 프로젝트 이름
### Django 서버 실행
python manage.py runserver
### Django 서버 종료
(키보드 누르기) ctrl + c
### Django 프로젝트 생성 루틴 정리 + git
1. 가상환경 생성
2. 가상환경 활성화
3. Django 설치
4. 의존성 파일 생성(패키지 설치마다 진행)
5. .gitignore 파일 생성 (첫 add 전)
6. git 저장소 생성
7. Django 프로젝트 생성
### 앱 생성 (앱의 이름은 복수형으로 지정하는 것을 권장)
python manage.py startapp articles
--------여기까지가 명령어 / 여기는 앱 이름
### 앱 등록
* 반드시 앱을 생성한 후에 등록해야 함
* 등록 후 생성은 불가능
1. 내가 생성한 프로젝프 폴더에 있는 seetings.py를 켜기
2. INSTALLED_APPS라는 리스트 가장 위에 내가 생성한 앱의 이름을 붙여넣기
### 디자인 패턴
소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책  
(공통적인 문제를 해결하는 데 쓰이는 형식화 된 관행)
### MVC 디자인 패턴
(Model, View, Controller)  
애플리케이션을 구조화하는 대표적인 패턴  
(데이터, 사용자 인터페이스, 비즈니스 로직을 분리)
* 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지보수할 수 있는 애플리케이션을 만들기 위해
### MTV 디자인 패턴
(Model, Template, View)
Django에서 애플리케이션을 구조화하는 패턴  
(기존 MVC 패턴과 동일하나 명칭을 다르게 정의한 것)
### 프로젝트 구조
1. settings.py : 프로젝트의 모든 설정을 관리
2. urls.py : URL과 이에 해당하는 적절한 views를 연결
3. admin.py : 관리자용 페이지 설정
4. models.py : DB와 관련된 Model을 정의, MTV 패턴의 M
5. views.py : HTTP요청을 처리하고 해당 요청에 대한 응답을 반환(url, mode, template과 연계), MTV 패턴의 V
### Django와 요청 and 응답
client(크롬) --> urls.py --> views.py <---> models.py  
client(크롬) <-------------- views.py <---> templates
### urls.py 안의 path라는 함수의 의미
처음 넣는 변수는 입력받는 문자열이고, 두번째 변수는 콜백함수, 로직이다.
### 직접 생성하는 파일
1. articles 안에 templates 폴더
2. urls.py
3. forms.py
### render함수
render(request, 템플릿위치, data)
1. request : 응답을 생성하는 데 사용되는 요청 객체
2. template_name : 템플릿 이름의 경로
3. context : 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)
  - 반드시 키 값과 벨류값의 변수명을 같게 하기
### Django Template system
데이터 표현을 제어하면서, 표현과 관련된 부분을 담당
### Django Template Language (DTL)
Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
1. Variable
  - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
  - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
  - dot(.)를 사용하여 변수 속성에 접근할 수 있음
2. Filters
  - 표시할 변수를 수정할 때 사용
  - chained가 가능하며 일부 필터는 인자를 받기도 함
  - 약 60개의 built-in template filters를 제공
3. Tags
  - 반복 또는 논리를 수행하여 제어 흐름을 만듦
  - 일부 태그는 시작과 종료태그가 필요함
  - 약 24개의 built-in template tags를 제공
### 템플릿 상속
페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton'템플릿을 작성하여 상속 구조를 구축
### block 블락의 이름
상속할 부모의 어느 위치에 내용을 채울지 block과 block의 이름으로 지정  
상속받은 자식은 블락과 블락의 이름을 설정한 뒤 그 안의 내용을 채우면 된다.
```html
{% block 블락이름 %}{% endblock 블락이름 %}
```
### extends 태그 {% extends "articles/base.html" %}
자식템플릿이 부모 템플릿을 확장한다는 것을 알림  
반드시 템플릿 최상단에 작성되어야함 (2개 이상 사용 불가)
```html
{% extends 주소위치 %}
```
### action 과 method
데이터를 어디로(action) 어떤 방식(method)으로 요청할지
```html
# throw.html
{% block content %}
<h1>fake naver</h1>
  <form action="/catch/" method='GET'>
    <label for="message">message : </label>
    <input type="text" name='message' id='message'>
    <input type="submit">
  </form>
{% endblock content %}

# catch.html
{% extends "articles/base.html" %}

{% block content %}
<h1>Throw로 부터 {{message}}를 받았다!!!</h1>
{% endblock content %}
```
### HTTP request 객체
form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨 있음(view함수의 첫번째 인자)
```python
def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'articles/catch.html', context)
```
### 'input' 요소
사용자의 데이터를 입력 받을 수 있는 요소 (type 속성 값에 따라 다양한 유형의 입력 데이터를 받음)
### 'name' attribute (입력 데이터에 붙이는 이름(key))
데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음
### 만약 앱 내부의 templates를 외부에서 탐색하고 싶을때
settings 내부의 코드를 수정한다.  
DIRS를 공란에서 아래 코드로 바꾼다.
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
```
### Variable Routing
URL 일부에 변수를 포함시키는 것 (변수는 view함수의 인자로 전달 할 수 있음)
### Variable routing 작성법
```python
path('hello/<str:name>/', views.greeting),
path('articles/<int:num>', views.detail),
path('<str:name>/<int:num>/', views.detail),

# 이름과 숫자는 반드시 해당 함수의 인자로 받아줘야한다.
def greeting(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/greeting.html', context)

def detail(request, num):
    context = {
        'num' : num
    }
    return render(request, 'articles/detail.html', context)

def detail(request, name, num):
    context = {
        'name' : name,
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)
```
### URL dispatcher (url 분배기)
url 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)
### Variable routing
```python
# 페이지가 많아질 경우 일일이 주소명을 지어줄 수 없으므로 변수명을 입력함
# 앱의 url들 끼리 
path('<str:user_id>/<int:article_pk>/', views.detail, name='detail')
```