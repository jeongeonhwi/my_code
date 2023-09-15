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
3. pip install -r django
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
### Django Model
db의 테이블을 정의하고 데이터를 조작(생성/수정/삭제)할 수 있는 기능들을 제공  
테이블 구조를 설계하는 '청사진(blueprint)
### model 클래스
```python
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  # 작성한 위의 모델 클래스는 최종적으로 DB에 다음과 같은 테이블 구조를 만듦
  # 앱 내부의 models.py파일 내부에 작성함.
```
* 클래스 변수명
 - 테이블의 각 '필드(열)' 이름
### Migrations 과정
model class(설계도 초안) --(makemigrations)--> migration 파일(최종 설계도) --(migrate)--> db.sqlite3(DB)
* Migrations 핵심 명령어 2가지
```bash
$ python manage.py makemigrations
# model class를 기반으로 최종 설계도(migration)작성

$ python manage.py migrate
# 최종 설계도를 DB에 전달하여 반영

# SQlite를 사용하면 데이터베이스를 오픈할 수 있다.
```
### 추가 Migrations
이미 생성된 테이블에 필드를 추가해야 한다면?  
```python
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  # 여기서부터 추가
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```
* 변경을 하고 makemigrations 명령어를 내리면 option을 선택하라고 말한다.
* 1번 입력은 현재 대화를 유지하면서 직접 기본값을 입력하는 방법
* 2번 입력은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법
* 추가하는 기본값은 장고가 제안하는 기본값을 사용하는 것을 권장 그냥 엔터누르면 된다.
### 추가 Migrations 순서
1. model class에 변경사항이 생겼다.
2. 새로운 설계도 생성 : makemigrations
3. DB에 반영하기 : migrate
### Model Field
DB 테이블의 필드(열)을 정의하며 해당 필드에 저장되는 데이터 타입과 제약조건을 정의
### CharField()
길이의 제한이 있는 문자열을 넣을 때 사용  
(필드의 최대 길이를 결정하는 max_length는 필수 인자. 없으면 작동안함)
### TextField()
글자의 수가 많을 때 사용
### DateTimeField()
날짜와 시간을 넣을 때 사용  
* DateTimeField의 선택인자
1. auto_now : 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장
2. auto_now_add : 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장

### Automatic admin interface
Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공  
데이터 확인 및 테스트 등을 진행하는데 매우 유용
### admin 계정 생성
```bash
$ python manage.py createsuperuser
```
### admin에 모델 클래스 등록
```python
from django.contrib import admin
#명시적 상대경로
from .models import Article
# Register your models here.

# Article 모델 사이트를 admin site에 등록
# admin site에 등록(register)한다. 
admin.site.register(Article)

# admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능
```
### 데이터베이스 초기화
1. migration 파일 삭제
2. db.sqlite3파일 삭제
* **migrations폴더나 init.py 파일을 지우지 않도록 주의**
### Migrations 기타 명령어
```bash
$ python manage.py showmigrations
# migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어
# [X] 표시가 있으면 migrate가 완료되었음을 의미

$ python manage.py sqlmigrate articles 0001
# 어떤 앱에 몇번째 설계도 인지를 맨 끝 두 단어에 적용
# 해당 migrations 파일이 SQL 언어(DB에서 사용하는 언어)로
# 어떻게 번역되어 DB에 전달되는지 확인하는 명령어
```
### form action 주소 넣는 방법
```html
<!-- 평소에는 액션 안에 /주소/를 직접 넣었지만 -->
<form action="/주소/" method='GET'>

<!-- 앱 이름과 패스의 이름으로 주소를 설정해줌 -->
<form action="{% url "throw_catch:throw_catch1" %}" method='GET'>
```
### ORM
객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술
### QuerySet API
ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구  
- API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리
### QuerySet API 구문
modelclass.manager.QuerySet API  
== Article.objects.all()
### Query
* 데이터베이스에 특정한 데이터를 보여달라는 요청
* 쿼리문을 작성한다. --> 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
* 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달
### QuerySet
* 데이터베이스에게서 전달받은 객체 목록(데이터 모음) : 순회가 가능한 데이터
* Django ORM을 통해 만들어진 자료형
* 단, 데이터베이스가 단일한 객체를 반환 할 때는 Queryset이 아닌 모델(class)의 인스턴스로 반환됨
### QuerySet API 실습 사전 준비
```bash
$ pip install ipython
$ pip install django-extensions
$ pip freeze > requirements.txt
```
### 앱 등록 권장 순서
```python
INSTALLED_APPS = [
    # app 등록 권장 순서
    # 1. normal app
    'articles',
    # 2. third party app
    'django_extensions',
    # 3. django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
### Django shell
Django 환경 안에서 실행되는 python shell  
(입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침)
```bash
$ python manage.py shell_plus
```
### 터미널 정리하는법
키보드 ctrl + L
### 데이터 객체를 만드는 방법
```bash
# class로부터 instance 생성
>>> article = Article()

# 인스턴스 변수(title)에 값을 할당
>>> article.title = 'first'

# 인스턴스 변수(content)에 값을 할당
>>> article.content = 'django!'

# 저장
>>> article.save()
```
### QuerySet API 실습
1. all()
- 전체 데이터 조회
2. get()
- 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
- 위와 같은 특징을 가지고 있기 때문에 pk(primary key)와 같이 고유성을 보장하는 조회에서 사용해야함.
3. filter()
- 특정 조건 데이터 조회
4. save()
- 객체를 데이터베이스에 저장하는 메서드
- 자료를 찾던, 한개 찾던, 세개찾던 쿼리셋으로 리턴한다.
### 데이터 수정
인스턴스 변수를 변경 후 save 메서드 호출
```bash
# 수정할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# 인스턴스 변수를 변경
>>> article.title = 'bye'

# 저장
>>> article.save()
```
### 데이터 삭제
삭제하려는 데이터 조회 후 delete 메서드 호출
```bash
# 삭제할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# 데이터 삭제
>>> article.delete()
```
### url의 path 내부의 주소에는 .을 쓰고 render 내부의 html참조하는 주소에는 /를 쓰는 이유
path에서 참조하는 앱폴더는 내부에 init파일이 있어 패키지로 인식된다.