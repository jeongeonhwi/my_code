# javascript
## Introduction of JavaScript
### History of JavaScript
#### 웹 브라우저와 JavaScript
* 웹의 탄생 (1990)
  - 팀 버너스리 경이 www, 하이퍼텍스트 시스템 고안
  - URL, HTTP 최초 설계 및 구형
  - 초기의 웹은 정적인 텍스트 페이지만을 지원
* 웹 브라우저의 대중화 (1993)
  - Netscape사의 최초 상용 웹 브라우저인 Netscape Navigator 출시
  - 당시 약 90% 이상의 시장 점유율을 가짐
* JavaScript의 탄생 (1995)
  - 당시 Netscape 소속 개발자 Brandon Eich는 웹의 동적 기능 개발이라는 회사의 요구사항을 넘어 스크립트 언어 Mocha를 개발
  - 이후 LiveScript로 이름을 변경 했으나 당시 가장 인기있던 프록래밍 언어인 Java의 명성에 기대보고자 JavaScript로 이름을 변경
  - JavaScript는 Netscape Navigator 2.0에 탑재되어 웹 페이지에 동적 기능을 추가하는 데 사용됨
* JavaScript 파편화 (1996)
  - Microsoft가 자체 웹 브라우저인 인터넷 익스플로러 3.0에 JavaScript와 유사한 언어인 JScript를 도입
  - 이 과정에서 많은 회사들이 자체적으로 JavaScript를 독자적으로 변경하고 이를 자체 브라우저에 탑재
* 1차 브라우저 전쟁 (1995-2001)
  - Netscape vs Microsoft
  - Microsoft는 IE를 자사 윈도우 운영체제에 내장하여 무료로 배포
  - 빌 게이츠를 필두로 한 Microsoft의 공격적인 마케팅, 자금력 그리고 윈도우 운영체제 점유율 앞에 Netscape는 빠르게 몰락하기 시작
  - IE의 시장 점유율은 2002년 약 96%에 달하며 Microsoft가 승리
  - 추후 Brandon Eich와 함께 Netscape에서 나온 핵심 개발진은 모질라 재단을 설립하여 Firefox 브라우저를 출시(2003)
* 2차 브라우저 전쟁 (2004-2017)
  - IE vs Crome vs Firefox
  - google의 chrome 브라우저 출시(2008)
  - 크롬은 출시 3년만에 파이어폭스의 점유율을 넘어서고 그로부터 반년 뒤 IE의 점유율을 넘어섬
* 2차 브라우저 전쟁의 영향
  - 웹 표준을 준수하는 Chrome의 등장으로 웹 표준의 중요성이 대두
  - 웹의 기능이 크게 확장되며 웹 애플리케이션의 비약적인 발전을 이끌어 감

#### ECMAScript
* JavaScript의 현재
  - 현재 chrome, firefox, safari, microsoft edge 등 다양한 웹 브라우저가 출시되어 있으며, 웹 브라우저 시장이 다양화 되어있음
  - 기존에 javascript는 브라우저에서만 웹 페이지의 동적인 기능을 구현하는 데에만 사용되었음
  - 이후 브라우저에서 벗어나 Node.js와 같은 서버 사이드 분야 뿐만 아니라, 다양한 프레임워크와 라이브러리들이 개발되면서, 웹 개발 분야에서는 필수적인 언어로 자리 잡게 됨
### JavaScript and DOM
#### DOM
* 웹 브라우저에서의 JavaScripts
  - 웹 페이지의 동겆인 기능을 구현
* JavaScript 실행 환경 종류
  1. HTML script 태그
  2. js 확장자 파일
  ```html
  <!-- hello.js 내부 -->
  console.log('hello')

  <!-- hello.html 내부 -->
  <body>
  <script src="hello.js"></script>
  <script>
    // console.log('hello')
  </script>
  </body>
  ```
  3. 브라우저 Console에 직접입력
    - console.log('hello')
* DOM
  - 웹 페이지(Document)를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
  - 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함
* DOM 특징
  - DOM에서 모든 요소, 속성, 텍스트는 하나의 객체
  - 모두 document 객체의 자식으로 구성됨
* DOM tree
  - 브라우저는 HTML 문서를 해석하여 DOM tree라는 객체 트리로 구조화
  - 객체 간 상속 구조가 존재
* DOM 핵심
  - 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API
* document 객체
  - 웹 페이지 객체
  - DOM Tree의 진입점
  - 페이지를 구성하는 모든 객체 요소를 포함
#### DOM 선택
* DOM 조작 시 기억해야 할 것
  - 웹 페이지를 동적으로 만들기 == 웹 페이지를 조작하기
  - 조작순서
    1. 조작 하고자 하는 요소를 선택 (또는 탐색)
    2. 선택된 요소의 콘텐츠 또는 속성을 조작
* 선택 메서드
  - document.querySelector()
    - 요소 한 개 선택
  - document.querySelectorAll()
    - 요소 여러 개 선택
* document.querySelector(selector)
  - 제공한 선택자와 일치하는 element 한 개 선택
  - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null 반환)
* document.querySelectorAll(selector)
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 제공한 CSS selector를 만족하는 NodeList를 반환
```html
<body>
  <h1 class="heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>
  <script>
    console.log(document.querySelector('.heading'))
    console.log(document.querySelector('.content'))
    console.log(document.querySelectorAll('.content'))
    console.log(document.querySelectorAll('ul > li'))
    // 굉장히 깊은 곳에 위치한 요소를 선택할 땐 개발자 도구에서 copy/selector 누르면 된다
    'body > p:nth-child(4)'
  </script>
</body>
```
#### DOM 조작
* 속성(attribute) 조작
1. 클래스 속성 조작
  - 'classList' property : 요소의 클래스 목록을 DOMTotenList(유사 배열) 형태로 반환
    - element.classList.add() : 지정한 클래스 값을 추가
    - element.classList.remove() : 지정한 클래스 값을 제거
    - element.classList.toggle() : 클래스가 존재한다면 제거하고 false를 반환 ( 존재하지 않으면 클래스를 추가하고 true 반환)
2. 일반 속성 조작
  - element.getAttribute() : 해당 요소에 지정된 값을 반환 (조회)
  - element.setAttribute(name, value) : 지정된 요소의 속성 값을 설정, 속성이 이미 있으면 기존 값을 갱신 (그렇지 않으면 지정된 이름과 값으로 새 속성이 추가)
  - element.removeAttribute() : 요소에서 지정된 이름을 가진 속성 제거
* DOM 요소 조작 메서드
  - document.createElement(tagName)
    - 작성한 tagName의 HTML 요소를 생성하여 반환
  - Node.appendChild()
    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    - 추가된 Node 객체를 반환
  - Node.removeChild()
    - Dom에서 자식 Node를 제거
    - 제거된 Node를 반환  
* style 조작
  - 'style' property : 해당 요소의 모든 style 속성 목록을 포함하는 속성
#### Node
* DOM의 기본 구성 단위
* DOM 트리의 각 부분은 Node라는 객체로 표현됨
  - Document Node => HTML 문서 전체를 나타내는 노드
  - Element Node => HTML 요소를 나타내는 노드 ex) <p>
  - Text Node => HTML 텍스트, Element Node 내의 텍스트 컨텐츠를 나타냄
  - Attribute Node => HTML 요소의 속성을 나타내는 노드
#### NodeList
* DOM 메서드를 사용해 선택한 Node의 목록
* 배열과 유사한 구조를 가짐
* Index로만 각 항목에 접근 간으
* 다양한 배열 메서드 사용 가능
* querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음
#### Element
* Node의 하위 유형
* Element는 DOM 트리에서 HTML 요소를 나타내는 특별한 유형의 Node
* 예를들어, <p>, <div>, <span>, <body> 등의 HTML 태그들이 Element 노드를 생성
* Node의 속성과 메서드를 모두 가지고 있으며 추가적으로 요소 특화된 기능을 가지고 있음 예) className, innerHTML, id 등
* 모든 Element는 Node이지만, 모든 Node가 Element인 것은 아님
#### DOM 속성 확인 Tip
* 개발자도구 - Elements - Properties
* 해당 요소의 모든 DOM 속성 확인 가능
## 자바스크립트 문법
### 변수
#### 식별자(변수명) 작성 규칙
* 반드시 문자, 달러 또는 밑줄로 시작
* 대소문자를 구분
* 예약어 사용 불가
  - for, if, function 등
* 카멜 케이스(camelCase)
  - 변수, 객체, 함수에 사용
* 파스칼 케이스(PascalCase)
  - 클래스, 생성자에 사용
* 대문자 스네이크 케이스(SNAKE_CASE)
  - 상수(constants)에 사용
#### let
* 블록 스코프(block scope)를 갖는 지역 변수를 선언
* 재할당 가능
* 재선언 불가능
* ES6에 추가
```html
let number = 10  <!-- 1. 선언 및 초기값 할당 -->
number = 20  <!-- 2. 재할당 -->

let number  = 10 <!-- 1. 선언 및 초기값 할당 -->
let number = 20  <!-- 2. 재할당 불가능 -->
```
#### const
* 블록 스코프를 갖는 지역 변수를 선언
* 재할당 불가능
* 재선언 불가능
* ES6에서 추가
```html
const number = 10  <!-- 1. 선언 및 초기값 할당 -->
number = 20  <!-- 2. 재할당 불가능 -->

const number  = 10 <!-- 1. 선언 및 초기값 할당 -->
const number = 20  <!-- 2. 재할당 불가능 -->
```
#### 블록 스코프 (block scope)
* if, for, 함수 등의 중괄호 내부를 가리킴
* 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
```html
<script>
      let x = 1

    if (x === 1) {
      let x = 2   // 2

      console.log(x)
    }

    console.log(x)   // 1
</script>
```
#### 변수 선언 키워드 정리
* 기본적으로 const 사용을 권장
* 재할당이 필요한 변수는 let으로 변경해서 사용
### 데이터 타입
#### 원시 자료형 (Primitive type)
* 변수에 값이 직접 저장되는 자료형  (불변, 값이 복사)
* 변수에 할당될 때 값이 복사됨
* 변수 간에 서로 영향을 미치지 않음
```html
  <script>
    let a = 10
    let b = a
    b = 20
    console.log(a) // 10
    console.log(b) // 20
  </script>
```
#### 참조 자료형 (Reference type)
* 객체의 주소가 저장되는 자료형  (가변, 주소가 복사)
* 객체를 생성하면 객체의 메모리 주소를 변수에 할당
* 변수 간에 서로 영향을 미침
```html
  <script>
    const obj1 = { name: 'Alice', age:30 }
    const obj2 = obj1
    obj2.age = 40

    console.log(obj1.age) // 40
    console.log(obj2.age) // 40
  </script>
```
#### 원시자료형 세부내용
* Number : 정수 또는 실수형 숫자를 표현하는 자료형
* string : 텍스트 데이터를 표현하는 자료형
  - '+' 연산자를 사용해 문자열끼리 결합
  - 곱셈, 나눗셈, 뺄셈 불가능
* Template literals(템플릿 리터럴) == 파이썬 f-string
  - 내장된 표현식을 허용하는 문자열 작성 방식
  - Backtick(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있음
  - 표현식은 '$'와 중괄호로 표기
  - ES6+ 부터 지원
  ```html
    <script>
      const age = 100
    const message = `홍길동은 ${age}세입니다.`
    console.log(message)   // 홍길동은 100세입니다.
    </script>
  ```
* null
  - 변수의 값이 없음을 의도적으로 표현할 때 사용
* undefined
  - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨
* Boolean
  - true / false
  - 조건문 또는 반복문에서 Boolean이 아닌 데이터 타입은 '자동 형변환 규칙'에 따라 true or false로 변환됨

|데이터 타입|false|true|
|---|---|----|
|undefined|항상 false|x|
|null|항상 false|x|
|Number|0,-0, NaN|나머지 모든 경우|
|string|빈문자열|나머지 모든 경우|

### 연산자
#### 할당 연산자
* 오른쪽에 잇는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
* 단축 연산자 지원
```html
<script>
  let a = 0
  a += 10
  a -= 3
  a *= 10
  a %= 7
  a /= 2
</script>
```
#### 비교 연산자
* 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과 값을 boolean으로 반환하는 연산자
```html
<script>
  3 > 2 //true
  3 < 2 //false
  'a'<'b' //true
  '가'>'나' //false
</script>
```
#### 일치 연산자 (===)
* 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
* 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
* 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
* 특수한 경우를 제외하고는 동등 연산자가 아닌 **일치 연산자 사용을 권장**
```html
<script>
  console.log(1 === 1) // true
  console.log('1' === '1') // true
  console.log('1' === 1) // false
  console.log(0 === false) // false
</script>
```
#### 논리 연산자
* and 연산 : &&
* or 연산 : ||
* not 연산 : !
* 단축 평가 지원
### 조건문
* if 
  - 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단
#### if 예시
```html
<script>
  const name = 'customer'

  if (name === 'admin') {
    console.log('관리자님')
  } else if (name === 'customer') {
    console.log('고객님')
  } else {
    console.log( `반갑습니다. ${name}`)
  }
</script>
```
#### 조건 (삼항) 연산자
* 세 개의 피연산자를 받는 유일한 연산자
* 앞에서부터 조건문, 물음표(?), 조건문이 참일 경우 실행할 표현식, 콜론(:), 조건문이 거짓일 경우 실행할 표현식이 배치
```html
<script>
  const func1 = function (person) {
    if (person > 17) {
      return 'Yes'
    } else {
      return 'No'
    }
  }

  // 위와 동일함

  const func2 = function (person) {
      return person > 17 ? 'Yes' : 'No'
  }
</script>
```
### 반복문
#### While
* 조건문이 참이면 문장을 계속해서 수행
```html
<script>
  let i = 0

  while (i < 6) {
    console.log(i)
    i += 1
  }
</script>
```
#### for
* 특정한 조건이 거짓으로 판별될 때까지 반복
```html
<script>
  for (let i = 0; i < 6; i++) {
    console.log(i)
  }
</script>
```
#### for...in
* 순서를 보장 안함
* 객체의 열거 가능한 속성(property)에 대해 반복
```html
<script>
  const fruits = { a:'apple', b:'banana' }

  for (const property in fruits) {
    console.log(property) // a, b
    console.log(fruits[property]) // apple, banana
  }
</script>
```
#### for...of
* 반복 가능한 객체(배열, 문자열 등)에 대해 반복
* object인 딕셔너리는 오류가 나온다.
```html
<script>
  const numbers = [0,1,2,3]

  for (const number of numbers) {
    console.log(number) // 0,1,2,3
  }
</script>
```
#### 반복문 사용 시 const 사용 여부
* for 문
  - for문의 경우에는 최초 정의한 i를 재할당하면서 사용하기 때문에 **const를 사용하면 에러발생**
* for...in, for...of
  - 재할당이 아니라, 매 반복마다 다른 속성 이름이 변수에 지정되는 것이므로 **const를 사용해도 에러가 발생하지 않음**
  - 단, const 특징에 따라 블록 내부에서 변수를 수정할 수 없음

|키워드|연관 키워드|스코프|
|--|--|--|
|while|break, continue|블록 스코프|
|for|break, continue|블록 스코프|
|for...in|object 순회|블록 스코프|
|for...of|lterable 순회|블록 스코프|

#### 배열인지 아닌지 판단하는 내장 객체
* Array.isArray(판별하고싶은변수) : 해당 내용을 true, false로 반환
* 찾고 싶은 내용이 있을 시 mdn 공식 도큐 참조 바람