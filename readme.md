# Vue
## Introduction of Vue
### Front-end Development
#### Front-end Development
* 웹사이트와 웹 애플리케이션의 사용자 인터페이스(UI)와 사용자 경험(UX)을 만들고 디자인하는 것
  - HTML, CSS, JavaScript 등을 활용하여 사용자가 직접 상호작용하는 부분을 개발
#### Client-side frameworks
* 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JavaScript 기반 프레임 워크
* 유명한 프레임워크
1. Angular js
2. vue js
3. react js
#### Client-side frameworks 가 필요한 이유 1/2
* 사용자는 이제 웹에서 문서만을 읽는 것이 아닌 음악을 스트리밍하고, 영화를 보고, 원거리에 있는 사람들과 텍스트 및 영상 채팅을 통해 즉시 통신하고 있음
* 이처럼 현대적이고 복잡한 대화형 웹 사이트를 **웹 애플리케이션(web applications)**이라 부름
* JavaScript 기반의 Client-side frameworks의 출현으로 매우 동적인 대화형 애플리케이션을 훨씬 더 쉽게 구축할 수 있게 됨
#### Client-side frameworks가 필요한 이유 2/2
* 웹에서 하는일이 많아 졌다.
  - 다루는 데이터가 많아졌다.
* 만약 친구가 이름을 변경했다면?
* 친구 목록, 타임라인, 스토리 등 친구 이름이 출력되는 모든 곳이 함께 변경되어야 함
* 애플리케이션의 기본 데이터를 안정적으로 추적하고 업데이트(렌더링, 추가, 삭제 등)하는 도구가 필요
  - **애플리케이션의 상태를 변경할 때마다 일치하도록 UI를 어베이트해야 한다는 것**
#### JavaScript만으로 모든 데이터를 조작한다면
* 어마어마한 불필요한 코드가 반복된다.
#### Single Page Application
* 페이지 한개로 구성된 웹 애플리케이션
1. 서버로부터 필요한 모든 정적 HTML을 처음에 한번 가져옴
2. 브라우저가 페이지를 로드하면 Vue 프레임워크는 각 HTML 요소에 적절한 JavaScript코드를 실행(이벤트에 응답, 데이터 요청 후 UI업데이트 등)
    - ex) 페이지 간 이동 시, 페이지 갱신에 필요한 데이터만을 JSON으로 전달받아 페이지 일부 갱신 
    - Google Maps, 인스타그램 등의 서비스에서 갱신 시 새로고침이 없는 이유
* 웹 애플리케이션의 초기 로딩 후 새로운 페이지 요청 없이 동적으로 화면을 갱신하며 사용자와 상호작용하는 웹 애플리케이션
  - CSR 방식
#### Client-side Renderiong (CSR)
* 클라이언트에서 화면을 렌더링 하는 방식
#### Client-side Rendering 방식
1. 브라우저는 페이지에 필요한 최소한의 HTML 페이지와 JavaScript를 다운로드 
2. 그런 다음 JavaScript를 사용하여 DOM을 업데이트하고 페이지를 렌더링
#### Client-side Rendering 장점
* 빠른 속도
  - 페이지의 일부를 다시 렌더링할 수 있으므로 동일한 웹 사이트의 다른 페이지로 이동하는 것이 일반적으로 더 빠름
  - 서버로 전송되는 데이터의 양을 최소화
* 사용자 경험
  - 새로고침이 발생하지 않아 네이티브 앱과 유사한 사용자 경험을 제공
* Front-end와 Back-end의 명확한 분리
  - Front-end는 UI 렌더링 및 사용자 상호 작용 처리를 담당 & Back-end는 데이터 및 API 제공을 담당
  - 대규모 애플리케이션을 더 쉽게 개발하고 유지 관리 가능
#### Client-side Rendering 단점
* 초기 구동속도가 느림
  - 전체 페이지를 보기 전에 약간의 지연을 느낄 수 있음
  - JavaScript가 다운로드, 구문 분석 및 실행될 때까지 페이지가 완전히 렌더링 되지 않기 때문
* SEO(검색 엔진 최적화) 문제
  - 페이지를 나중에 그려 나가는 것이기 때문에 검색에 잘 노출되지 않을 수 있음
### Vue
#### What is Vue
* 사용자 인터페이스를 구축하기 위한 JavaScript 프레임워크
* 2014년 발표 - Evan You
  - 학사-미술, 미술사 / 석사-디자인 & 테크놀로지 전공 / Angular 개발팀 출신
* 2023년 기준 최신 버전은 'Vue 3'
  - https://vuejs.org/
* **Vue 2 문서에 접속하지 않도록 주의**
#### Vue를 학습하는 이유
* 쉬운 학습 곡선 및 간편한 문법
  - 새로운 개발자들도 빠르게 학습할 수 있음
* 반응성 시스템
  - 데이터 변경에 따라 자동으로 화면이 업데이트되는 기능을 제공
* 모듈화 및 유연한 구조
  - 애플리케이션을 컴포넌트 조각으로 나눌 수 있음
  - 코드의 재사용성을 높이고 유지보수를 용이하게 함
#### Vue의 2가지 핵심 기능
```html
<body>

  <div id="app">
    <h1>{{ greeting }}</h1>
    <button @click="count++">{{ count }}</button>
    <p>{{ count }}</p>
    <h3>{{ count }}</h3>
  </div>

  <!-- <div id="app">{{ message }}</div> -->
  
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const greeting = ref('Hello')
        return {
          count,
          greeting,
        }
      }
    })

    app.mount('#app')
  </script>
</body>
```
* 선언적 렌더링 (Declarative Rendering)
  - HTML을 확장하는 템플릿 구문을 사용하여 HTML이 JavaScript 데이터를 기반으로 어떻게 보이는지 설명할 수 있음
* 반응형 (Reactivity)
  - JavaScript 상태 변경사항을 자동으로 추적하고 변경사항이 발생할 때 DOM을 효율적으로 업데이트
#### 첫번째 Vue 작성하기 
* CDN Application instance 작성
  - 모든 Vue 애플리케이션은 createApp 함수로 새 Application instance를 생성하는 것으로 시작
* app.mount()
  - 컨테이너 요소에 애플리케이션 인스턴스를 탑재(연결)
  - 각 앱 인스턴스에 대해 mount()는 한 번만 호출할 수 있음
```html
    <div id="app"></div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({})

    app.mount('#app')
  </script>
```
#### ref()
* 반응형 상태(데이터)를 선언하는 함수 (Declaring Reactive State)
#### ref 함수 () 
* 인자를 받아 .value 속성이 있는 ref 객체로 래핑(wrapping)하여 반환
* ref로 선언된 변수의 값이 변경되면, 해당 값을 사용하는 템플릿에서 자동으로 업데이트
* 인자는 어떠한 타입도 가능
* 템플릿의 참조에 접근하려면 setup 함수에서 선언 및 반환 필요
* 템플릿에서 ref를 사용할 때는 .value를 작성할 필요 없음(automatically unwrapped)
```html
<body>
  <div id="app">
    <h1>{{ message }}</h1>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const message = ref('Hello vue!')
        console.log(message) // ref객체
        console.log(message.value) // Hello vue!
        return {
          message,
        }
      }
    })

    app.mount('#app')
  </script>
</body>
```
* 반응형을 가지는 참조 변수를 만드는 것(ref===reactive reference)
#### Vue 기본 구조
* createApp()에 전달되는 객체는 Vue 컴포넌트(Component)
* 컴포넌트의 상태는 setup() 함수 내에서 선언되어야 하며 **객체를 반환해야 함**
#### 템플릿 렌더링
* 반환된 객체의 속성은 템플릿에서 사용할 수 있음
* Nustache syntax(콧수염 구문)를 사용하여 메세지 값을 기반으로 동적 텍스트를 렌더링
* 콘텐츠ㅡㄴ 식별자나 경로에만 국한되지 않으며 유효한 JavaScript 표현식을 사용할 수 있음
```html
<h1>{{ message.split('').reverse().join('' )}}</h1>
```
#### Event Listeners in Vue
* 'v-on' directive를 사용하여 DOM 이벤트를 수신할 수 있음
* 함수 내에서 refs를 변경하여 구성 요소 상태를 업데이트
```html
<body>
  <div id="app">
    <button v-on:click="increment">{{ count }}</button>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const increment = function () {
          count.value++
        }
        return {
          count,
          increment
        }
      }
    })

    app.mount('#app')
  </script>
</body>
```
### Ref Unwrap 주의사항
#### 템플릿에서의 unwrap 시 주의사항 1/4
* 템플릿에서의 unwrap은 ref가 최상위 속성인 경우에만 적용가능
* 다음 표현식을 어떻게 출력될까?
```html
<script>
  const object = { id: ref(0) }
</script>
  {{ object.id + 1}}
```
* object는 최상위 속성이지만 object.id는 그렇지 않음
* 표현식을 평가할 때 object.id가 unwrap 되지 않고 ref 객체로 남아있기 때문
* 이문제를 해결하기 위해서는 id를 최상위 속성으로 분해해야 함
```html
<script>
  const { id } = object
</script>
  {{ id + 1}}
```
* **단, ref가 {{}}의 최종 평가 값인 경우는 unwrap 가능**
#### why Ref?
* 일반 변수 대신 굳이 .value가 포함된 ref가 필요한 이유는?
* Vue는 템플릿에서 ref를 사용하고 나중에 ref의 값을 변경하면 자동으로 변경 사항을 감지하고 그에 따라 DOM을 업데이트 함(의존성 추적 기반의 반응형 시스템)
* Vue는 렌더링 중에 사용된 모든 ref를 추적하며, 나중에 ref가 변경되면 이를 추적하는 구성 요소에 대해 다시 렌더링
  - JavaScript에서는 일반 변수의 접근 또는 변형을 감지할 방법이 없기 때문
#### SEO (Search Engine Optimization)
* google, bing과 같은 검색 엔진 등에 내 서비스나 제품 등이 효율적으로 검색 엔진에 노출되도록 개선하는 과정을 일컫는 작업
* 정보의 대상은 주로 HTML에 작성된 내용
* 검색
  - 각 사이트가 운용하는 검색 엔진에 의해 이루어지는 작업
* 검색엔진
  - 웹 상에 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작
* 최근에는 SPA, 즉 CSR로 구성된 서비스의 비중이 증가
* SPA 서비스도 검색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전하는 중
#### CSR & SSR
* CSR과 SSR은 흑과 백이 아님
  - 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
* SPA 서비스에서도 SSR을 지원하는 frameworks가 발전하고 있음
  - vue의 Nuxt.js
  - React의 Next.js
  - Angular Universal
## Basic Syntax - 01
### Template Syntax
#### Template Syntax
* DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문을 사용
#### Template Syntax 종류
1. Text Interpolation
2. Raw HTML
3. Attribute Bindings
4. JavaScript Expressions
#### 1. Text Interpolation
```html
<p>message: {{ msg }} </p>
```
* 데이터 바인딩의 가장 기본적인 형태
* 이중 중괄호 구문 (콧수염 구문)을 사용
* 콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
* msg 속성이 변경될 때마다 업데이트 됨
#### 2. Raw HTML
```html
<div v-html="rawHtml"></div>

<script>
  const rawHtml = ref('<span style="color:red">This should be red.</span>')
</script>
```
* 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야함
#### 3. Attribute Bindings
```html
<div v-bind:id="dynamicId"></div>

<script>
  const dynamicId = ref('my-id')
</script>
```
* 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 v-bind를 사용
* HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
* 바인딩 값이 null이나 undefind인 경우 렌더링 요소에서 제거됨
#### 4. JavaScript Expressions
```html
<div>{{ number + 1}}</div>
<div>{{ ok ? 'Yes' : 'No' }}</div>
<div>{{ msg.split('').reverse().join('') }}</div>
<div v-bind:id="`list-${id}`"></div>
```
* Vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
* Vue 템플릿에서 JavaScript 표현식을 사용할 수 있는 위치
  - 콧수염 구문 내부
  - 모든 directive의 속성 값 (v-로 시작하는 특수 속성)
#### Expressions 주의사항
* 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
  - 표현식은 값으로 평가할 수 있는 코드 조각(return 뒤에 사용할 수 있는 코드여야 함)
* 작동하지 않는 경우
```html
<!-- 표현식이 아닌 선언식 -->
{{ const number = 1 }}

<!-- 흐름제어도 작동하지 않음. 삼항 표현식을 사용 -->
{{ if (ok) { return message }}}
```
#### Directive
* 'v-' 접두사가 있는 특수 속성
#### Directive 특징
* Directive의 속성 값은 단일 JavaScript 표현식이어야 함(v-for, v-on 제외)
* 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용
* 예시
  - v-if 는 seen 표현식 값의 T/F를 기반으로 <p> 요소를 제거/삽입
```html
<p v-if="seen">Hi There</p>
```
#### Directive 전체 구문
* **v-on:submit.prevent="onSubmit"**
* v-on : Name
  - starts with v- Mab be omitted when using shorthands
* submit : Argument
  - Follows the colon or shorthand symbol
* prevent : Modifiers
  - Denoted by the leading dot
* onsubmit : Value
  - Interpreted as JavaScript expressions
#### Directive -Arguments
* 일부 directive는 directive 뒤에 콜론(:)으로 표시되는 인자를 사용할 수 있음 
* 아래 예시의 href는 HTML a 요소의 href 속성 값을 myUrl 값에 바인딩 하도록 하는 v-bind의 인자
```html
<p v-bind:href="myUrl">Link</p>
```
* 아래 예시의 click은 이벤트 수신할 이벤트 이름을 작성하는 v-on의 인자
```html
<button v-on:click="doSomething">Button</button>
```
#### Directive - Modifiers
* .(dot)로 표시되는 특수 접미사로, directive가 특별한 방식으로 바인딩되어야 함을 나타냄
* 예를 들어 .prevent는 발생한 이벤트에서 event.preventDefault()를 호출하도록 v-on에 지시하는 modifier
```html
<form @submit.prevent="onSubmit">...</form>
```
#### Built-in Directives
* v-text
* v-show
* v-if
* v-for
* ...
* 공식문서 참조
### Dynamically data binding
#### v-bind
* 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩
#### v-bind 사용처
1. Attribute Bindings
2. Class and Style Bindings
#### Attribute Bindings 1/2
* HTML의 속성 값을 Vue의 상태 속성 값과 동기화 되도록 함
```html
<img v-bind:src="imageSrc" alt="">
<a v-bind:href="myUrl">Link</a>
```
* v-bind shorthand (약어)
  - ':' (colon)
```html
<!-- 위와 같은 의미의 코드 -->
<img :src="imageSrc" alt="">
<a :href="myUrl">Link</a>
```
#### Attribute Bindings 2/2
* Dynamic attribute name (동적 인자 이름)
  - 대괄호로 감싸서 directive argument에 JavaScript 표현식을 사용할 수도 있음
  - JavaScript 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨
```html
<p :[dynamicattr]="dynamicValue"></p>

<script>
  // setup함수 안에 해당 내용을 넣어 자유롭게 속성값을 부여 가능
  const dynamicattr = ref('title')
  const dynamicValue = ref('Hello')
</script>
```
* **대괄호 안에 작성하는 이름은 반드시 소문자로만 구성 가능하다!!!**
#### Class and Style Bindings
* 클래스와 스타일은 모두 속성이므로 v-bind를 사용하여 다른 속성과 마찬가지로 동적으로 문자열 값을 할당할 수 있음
* 그러나 단순히 문자열 연결을 사용하여 이러한 값을 생성하는 것은 번거롭고 오류가 발생하기가 쉬움
* Vue는 클래스 및 스타일과 함께 v-bind를 사용할 때 객체 또는 배열을 활용한 개선 사항을 제공
#### Class and Style Bindings가 가능한 경우
* Binding HTML Classes
  - Binding to Objects
  - Binding to Arrays
* Binding Inline Styles
  - Binding to Objects
  - Binding to Arrays
#### Binding HTML Classes - Binding to Objects
* 객체를 :class에 전달하여 클래스를 동적으로 전환할 수 있음
* 예시 1
  - isActive의 T/F에 의해 active 클래스의 존재가 결정됨
```html
<div :class="{ active: isActive }">Text</div>
<div class="static" :class="{ active: isActive, 'text-primary':hasInfo }">Text</div>
<div class="static" :class="classObj">Text</div>

<script>
  // setup함수 안에 해당 내용을 넣어 자유롭게 속성값을 부여 가능
setup() {
  const isActive = ref(true)
  const hasInfo = ref(true)
  const classObj = ref({ 
    active: isActive, 
    'text-primary':hasInfo 
  })}
</script>
```
#### Binding HTML Classes - Binding to Arrays
* :class를 배열에 바인딩하여 클래스 목록을 적용할 수 있음
* 배열 구문 내에서 객체 구문도 사용가능
* 예시 1
```html
<div :class="[activeClass, infoClass]">Text</div>
<div :class="[{active: isActive}, infoClass]">Text</div>

<script>
setup() {
  const activeClass = ref('active')
  const infoClass = ref('text-primary')
  }
</script>
```
#### Binding Inline Styles - Binding to Objects
* :style은 JavaScript 객체 값에 대한 바인딩을 지원(HTML style 속성에 해당)
* 실제 CSS에서 사용하는 것처럼 :style은 kebab-cased 키 문자열도 지원(단, camelCase 작성을 권장)
* 예시1
```html
<div :style="{ color: activeColor, fontSize: fontSize + 'px'}">Text</div>

<script>
setup() {
  const activeColor = ref('crimson')
  const fontSize = ref(50)
  }
</script>
```
#### Binding Inline Styles - Binding to Objects 2
* 템플릿을 더 깔끔하게 작성하려면 스타일 객체에 직접 바인딩하는 것을 권장
```html
<div :style="styleObj">Text</div>

<script>
setup() {
  const activeColor = ref('crimson')
  const fontSize = ref(50)
  const styleObj = ref({
    color: activeColor,
    fontSize:fontSize.value + 'px'
  })
  }
</script>
```
#### Binding Inline Styles - Binding to Arrays
* 여러 스타일 객체의 배열에 :style을 바인딩할 수 있음
* 작성한 객체는 병합되어 동일한 요소에 적용
* 예시
```html
<div :style="[styleObj, styleObj2]">Text</div>

<script>
setup() {
  const activeColor = ref('crimson')
  const fontSize = ref(50)
  const styleObj = ref({
    color: activeColor,
    fontSize:fontSize.value + 'px'
  })
  const styleObj2 = ref({
    color: 'blue',
    border: '1px solid black',
  })
  }
</script>
```
### Event Handling
#### v-on
* DOM 요소에 이벤트 리스너를 연결 및 수신
#### v-on 구성
```html
v-on:event="handler"
```
* handler 종류
  - Inline handlers:이벤트가 트리거 될 때 실행 될 JavaScript 코드
  - Method handlers:컴포넌트에 정의된 메서드 이름
* v-on shorthand(약어)
  - '@'
```html
@event="handler"
```
#### Inline handlers
* Inline handlers는 주로 간단한 상황에 사용
```html
<script>
  const count = ref(0)
</script>

<button @click="count++">Add 1</button>
<p>Count: {{ count }}</p>
```
#### Method Handlers 1/2
* Inline handlers로는 불가능한 대부분의 상황에서 사용
* Method Handlers는 이를 트리거하는 기본 DOM Event 객체를 자동으로 수신
```html
<script>
const name = ref('Alice')
const myFunc = function (event) {
  console.log(event)
  console.log(event.currentTarget)
  console.log(`Hello ${name.value}!`)
}
</script>

<button @click="myFunc">Hello</button>
```
#### Inline Handlers에서의 메서드 호출
* 메서드 이름에 직접 바인딩하는 대신 Inline Handlers에서 메서드를 호출할 수도 있음
* 이렇게 하면 기본 이벤트 대신 사용자 지정 인자를 전달할 수 있음
```html
<script>
const greeting = function (message) {
  console.log(message)
}
</script>

<button @click="greeting('hello')">Say hello</button>
<button @click="greeting('bye')">Say bye</button>
```
#### Inline Handlers에서의 event 인자에 접근하기
* Inline Handlers에서 원래 DOM 이벤트에 접근하기
* event 변수를 사용하여 메서드에 전달
```html
<script>
const warning = function (message, evnet) {
  console.log(message)
  console.log(evnet)
}
</script>

<button @click="warning('경고합니다.', $event)">Submit</button>
```
#### Event Modifiers
* Vue는 v-on에 대한 Event Modifiers를 제공해 event.preventDefault()와 같은 구문을 메서드에서 작성하지 않도록 함
* stop, prevent, self 등 다양한 modifiers를 제공
  - 메서드는 DOM 이벤트에 대한 처리보다는 데이터에 관한 논리를 작성하는 것에 집중할 것
```html
<form @submit.prevent="onSubmit">
  <input type="submit">
</form>
<a @click.stop.prevent="onLink">Link</a>
```
* **Modifiers는 chained 되게끔 작성할 수 있으며 이때는 작성된 순서로 실행되기 때문에 작성 순서에 유의**
#### Key Modifiers
* Vue는 키보드 이벤트를 수신할 때 특정 키에 관한 별도 modifiers를 사용할 수 있음
* 예시
  - key가 Enter 일 때만 onSubmit 이벤트를 호출하기
```html
<input @keyup.enter="onSubmit">
```
### Form Input Bindings
#### Form Input Bindings
* form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JavaScript 상태에 동기화해야 하는 경우 (**양방향 바인딩**)
* 양방향 바인딩 방법
  - v-bind와 v-on을 함께 사용
  - v-model 사용
#### v-bind와 v-on을 함께 사용
* v-bind를 사용하여 input 요소의 value 속성 값을 입력 값으로 사용
* v-on을 사용하여 input 이벤트가 발생할 때마다 input 요소의 value 값을 별도 반응형 변수에 저장하는 핸들러를 호출
* v-bind를 사용하여 input 요소의 value 속성 값을 입력 값으로 사용
* v-on을 사용하여 input 이벤트가 발생 할 때마다 input 요소의 value 값을 별도 반응 형 변수에 저장하는 핸들러를 호출
```html
<script>
  setup() {
  const inputText1 = ref('')
  const onInput = function (event) {
    inputText1.value = event.currentTarget.value
  }}
</script>

<p>{{ inputText1 }}</p>
<input :value="inputText1" @input="onInput">
```
#### v-model
* form input 요소 또는 컴포넌트에서 양방향 바인딩을 만듦
#### v-model 사용
* v-model을 사용하여 사용자 입력 데이터와 반응형 변수를 실시간 동기화
```html
<script>
  setup() {
    const inputText2 = ref('')
  }
</script>

<p>{{ inputText2 }}</p>
<input v-model="inputText2">
```
* v-model을 사용하여 사용자 입력 데이터와 반응형 변수를 실시간 동기화
  - IME가 필요한 언어(한국어, 중국어, 일본어 등)의 경우 v-model이 제대로 업데이트되지 않음
  - 해당 언어에 대해 올바르게 응답하려면 v-bind와 v-on 방법을 사용해야 함
#### v-model과 다양한 입력(input) 양식
* v-model은 단순 text input 뿐만 아니라 Checkbox, Radio, Select 등 다양한 타입의 사용자 입력 방식과 함께 사용 가능
#### Checkbox 활용 1/2
* 단일 체크 박스와 boolean 값 활용
```html
<script>
  setup() {
    const checked = ref(false)
  }
</script>

<input type="checkbox" id="checkbox" v-model="checked">
<label for="checkbox">{{ checked }}</label>
```
#### Checkbox 활용 2/2
* 여러 체크박스와 배열 활용
  - 해당 배열에는 현재 선택된 체크박스의 값이 포함됨
```html
<script>
  setup() {
    const checkedNames = ref([])
  }
</script>

<div>Checked names: {{ checkedNames }}</div>

<input type="checkbox" id="alice" value="Alice" v-model="checkedNames">
<label for="alice">Alice</label>

<input type="checkbox" id="bella" value="Bella" v-model="checkedNames">
<label for="bella">Bella</label>
```
* 여러 체크박스와 배열 활용
  - 해당 배열에는 현재 선택된 체크박스의 값이 포함됨
#### Select 활용
* select에서 v-model 표현식의 초기 값이 어떤 option과도 일치하지 않는 경우 select 요소는 '선택되지 않은(unselected)' 상태로 렌더링 됨
```html
<script>
  setup() {
    const selected = ref('')
  }
</script>

<div>Selected: {{ selected }}</div>

<select v-model="selected">
  <option disabled value="">Please select one</option>
  <option>Alice</option>
  <option>Bella</option>
  <option>Cathy</option>
</select>
```
#### IME (Input Method Editor)
* 사용자가 입력 장치에서 기본적으로 사용할 수 없는 문자(비영어권 언어)를 입력할 수 있도록 하는 운영 체제 구성 프로그램
* 일반적으로 키보드 키보다 자모가 더 많은 언어에서 사용해야 함
  - IME가 동작하는 방식과 Vue의 양방향 바인딩(v-model) 동작 방식이 상충하기 때문에 한국어 입력 시 예상대로 동작하지 않았던 것
## Basic Syntax - 02
### Computed Property
#### computed()
* 계산된 속성을 정의하는 함수
  - 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄임
#### computed 기본예시
* 반응성 데이터를 포함하는 복잡한 로직의 경우 computed를 활용하여 미리 값을 계산
```html
<script>
        setup() {
        const todos = ref([
          { text: 'Vue 실습' },
          { text: '자격증 공부' },
          { text: 'TIL 작성' }
        ])

        const restOfTodos = computed(() => {
          return todos.value.length > 0 ? '아직 남았다.' : '퇴근!'
        })

        return {
          todos,
          restOfTodos,
        }
      }
</script>

<p>{{ restOfTodos }}</p>
```
#### computed 특징
* 반환되는 값을 computed ref이며 일반 refs와 유사하게 계산된 결과를 .value로 참조할 수 있음(템플릿에서는 .value 생략 가능)
* computed 속성은 의존된 반응형 데이터를 **자동으로 추척**
* 의존하는 데이터가 변경될 때만 재평가
  - restOfTodos의 계산은 todos에 의존하고 있음
  - 따라서 **todos가 변경될 때만 restOfTodos가 업데이트** 됨
#### computed와 동일한 로직을 처리할 수 있는 method
* computed 속성 대신 method로도 동일한 기능을 정의할 수 있음
* 두 가지 접근 방식은 실제로 완전히 동일
```html
<script>
          const getRestOfTodos = function () {
          return todos.value.length > 0 ? '아직 남았다.' : '퇴근!'
        }
</script>

<p>{{ getRestOfTodos() }}</p>
```
#### computed와 method 차이
* computed 속성은 **의존된 반응형 데이터를 기반으로 캐시(cached)된다**
* 의존하는 데이터가 변경된 경우에만 재평가됨
* 즉, 의존된 반응형 데이터가 변경되지 않는 한 이미 계산된 결과에 대한 여러 참조를 다시 평가할 필요 없이 이전에 계산된 결과를 즉시 반환
  - 반면, method 호출은 다시 렌더링이 발생할 때마다 항상 함수 실행
#### cache (캐시)
* 데이터나 결과를 일시적으로 저장해두는 임시 저장소
* 이후에 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근할 수 있도록 함
#### computed와 method의 적절한 사용처
* computed
  - 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
  - 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결고를 캐싱하여 중복 계산 방지
  - 의존된 데이터가 변경되면 자동으로 업데이트
* method
  - 단순한 특정 동작을 수행하는 함수를 정의할 때 사용
  - 데이터에 의존한는지 여부와 관계없이 항상 동일한 결과를 반환하는 함수
  - 호출해야만 실행됨
* **무조건 computed만 사용하는 것이 아니라 사용목적과 상황에 맞게 computed와 method를 적절히 조합하여 사용**
### Conditional Rendering
#### v-if
* 표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링
#### v-if 예시
```html
<script>
  const name = ref('Cathy')
</script>

  <div v-if="name === 'Alice'">Alice입니다</div>
  <div v-else-if="name === 'Bella'">Bella입니다</div>
  <div v-else-if="name === 'Cathy'">Cathy입니다</div>
  <div v-else>아무도 아닙니다.</div>
```
```html
<script>
  const isSeen = ref(true)
</script>

<p v-if="isSeen">true일때 보여요</p>
<p v-else>false일때 보여요</p>
<button @click="isSeen = !isSeen">토글</button>
```
#### 여러 요소에 대한 v-if 적용
* v-if는 directive이기 때문에 단일 요소에만 연결 가능
* 이경우 **template** 요소에 v-if를 사용하여 하나 이상의 요소에 대해 적용할 수 있음 (v-else, v-else-if 모두 적용 가능)
```html
<template v-if="name === 'Cathy'">
  <div>Cathy입니다</div>
  <div>나이는 30살입니다</div>
</template>
```
#### HTML template element
* 페이지가 로드 될 때 렌더링 되지 않지만 JavaScript를 사용하여 나중에 문서에서 사용할 수 있도록 하는 HTML을 보유하기 위한 메커니즘
* 보이지 않는 wrapper 역할
#### v-show
* 표현식 값의 T/F를 기반으로 요소의 가시성을 전환
#### v-show 예시
* v-show 요소는 항상 렌더링 되어 DOM에 남아있음
* CSS display 속성만 전환하기 때문
```html
<script>
  const isSeen = ref(true)
</script>

<p v-show="isSeen">v-show</p>
```
#### v-if vs v-show
* v-if (Cheap initial load, expensive toggle)
  - 초기 조건이 false인 경우 아무 작업도 수행하지 않음
  - 토글 비용이 높음
* v-show (Expensive initial load, cheap toggle)
  - 초기 조건에 관계 없이 항상 렌더링
  - 초기 렌더링 비용이 더 높음
* **무언가를 매우 자주 전환해야 하는 경우에는 v-show를, 실행 중에 조건이 변경되지 않는 경우에는 v-if를 권장 **
### List Rendering
#### v-for
* 소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링
#### v-for 구조
* v-for는 **alias in expression**형식의 특수 구문을 사용하여 반복되는 현재 요소에 대한 별칭(alias)을 제공
* 인덱스(객체에서는 키)에 대한 별칭을 지정할 수 있음
#### v-for 예시
* 배열반복
```html
<script>
  const myArr = ref([
    { name: 'Alice', age: 20 },
    { name: 'Bella', age: 21 }
  ])
</script>

<div v-for="(item, index) in myArr">
  {{ index }} / {{ item }}
</div>
```
#### v-for 예시 2
* 객체 반복
```html
<script>
  const myObj = ref({
    name: 'Cathy',
    age: 30
  })
</script>

<div v-for="(value, key, index) in myObj">
  {{ index }} / {{ key }} / {{ value }}
</div>
```
#### 여러 요소에 대한 v-for 적용
* template 요소에 v-for를 사용하여 하나 이상의 요소에 대해 반복 렌더링 할 수 있음
```html
<ul>
  <template v-for="item in myArr">
    <li>{{ item.name}}</li>
    <li>{{ item.age}}</li>
    <hr>
  </template>
</ul>
```
#### 중첩된 v-for
* 각 v-for 범위는 상위 범위에 접근 할 수 있음
```html
<script>
    const myInfo = ref([
    { name: 'Alice', age: 20, friends: ['Bella', 'Cathy', 'Dan'] },
    { name: 'Bella', age: 21, friends: ['Alice', 'Cathy'] }
  ])
</script>

<ul v-for="item in myInfo">
  <li v-for="friend in item.friends">
    {{ item.name}} - {{ friend }}
  </li>
</ul>
```
#### 반드시 v-for와 key를 함께 사용한다.
* 내부 컴포넌트의 상태를 일관되게 유지
  - 데이터의 예측 가능한 행동을 유지 (Vue 내부 동작 관련)
#### v-for와 key
* key는 반드시 각 요소에 대한 고유한 값을 나타낼 수 있는 식별자여야 함
```html
<script>
  const items = ref([
    { id: id++, name: 'Alice' },
    { id: id++, name: 'Bella' },
  ])
</script>

<div v-for="item in items" :key="item.id">
  <!-- content -->
  {{ item }}
</div>
```
#### 동일 요소에 v-for와 v-if를 함께 사용하지 않는다.
* 동일한 요소에 v-if가 v-for보다 우선순위가 더 높기 때문
  - v-if조건은 v-for 범위의 변수에 접근할 수 없음
#### v-for와 v-if 해결법 -1
* **computed를 활용해 필터링 된 목록을 반환하여 반복**하도록 설정
```html
<script>
  const completeTodos = computed(() => {
    return todos.value.filter((todo) => !todo.isComplete)
  })
</script>

<ul>
  <li v-for="todo in completeTodos" :key="todo.id">
    {{ todo.name }}
  </li>
</ul>
```
#### v-for와 v-if 해결법 2
* v-for와 template 요소를 사용하여 **v-if를 이동**
```html
<ul>
  <template v-for="todo in todos" :key="todo.id">
    <li v-if="!todo.isComplete">
      {{ todo.name }}
    </li>
  </template>
</ul>
```
### Watchers
#### watch()
* 반응형 데이터를 감시하고, 감시하는 데이터가 변경되면 콜백 함수를 호출
#### watch 구조
```html
<script>
  const countWatch = watch(variable, (newValue, oldValue) => {
    
  })
</script>
```
* variable
  - 감시하는 변수
* newValue
  - 감사하는 변수가 변화된 값
  - 콜백 함수의 첫번째 인자
* oldValue
  - 콜백 함수의 두번째 인자
#### watch 예시
```html
<script>
  const countWatch = watch(count, (newValue, oldValue) => {
    console.log(`newValue: ${newValue}, oldValue: ${oldValue}`)
  })
</script>

<button @click="count++">Add 1</button>
<p>Count: {{ count }}</p>
```
#### Computed와 Watchers
||Computed|Watchers|
|-|-|-|
|공통정|데이터의 변화를 감지하고 처리|
|동작|의존하는 데이터 속성의 계산된 값을 반환| 특정 데이터 속성의 변화를 감시하고 작업을 수행|
|사용 목적|템플릿 내에서 사용되는 데이터 연산용|데이터 변경에 따른 특정 작업 처리용|
|사용 예시|여산 된 길이, 필터링 된 목록 계산 등|비동기 API요청, 연관 데이터 업데이트 등|
* **computed와 watch 모두 의존(감시)하는 원본 데이터를 직접 변경하지 않음**
### Lifecycle Hooks
#### Lifecycle Hooks
* Vue 인스턴스의 생애주기 동안 특정 시점에 실행되는 함수
  - 개발자가 특정 단계에서 의도하는 로직이 실행될 수 있도록 함
```html
<script>
  onUpdated(() => {
    message.value = 'updated!'
  })
</script>

<div id="app">
  <button @click="count++">Add 1</button>
  <p>Count: {{ count }}</p>
  <p>{{ message }}</p>
</div>
```
#### Lifecycle Hooks 특징
* Vue는 Lifecycle Hooks에 등록된 콜백 함수들을 인스턴스와 자동으로 연결함
* 이렇게 동작하려면 hooks 함수들은 반드시 동기적으로 작성되어야 함
* 인스턴스 생애 주기의 여러 단계에서 호출되는 다른 hooks도 있으며, 가장 일반적으로 사용되는 것은 **onMounted, onUpdated, onUnmounted**
### Vue Style Guide
#### Vue Style Guide
* Vue의 스타일 가이드 규칙은 우선순위에 따라 4가지 범주로 나눔
* 규칙 범주
  - 우선순위 A:필수 (Essential)
  - 우선순위 B:적극 권장 (Strongly Recommended)
  - 우선순위 C:권장 (Recommended)
  - 우선순위 D:주의 필요 (Use with Caution)
* https://vuejs.org/style-guide/
#### 우선순위 별 특징
- A:필수 (Essential)
  - 오류를 방지하는 데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수
- B:적극 권장 (Strongly Recommended)
  - 가독성 및/또는 개발자 경험을 향상시킴
  - 규칙을 어겨도 코드는 여전히 실행되겠지만, 정당한 사유가 있어야 규칙을 위반할 수 있음
- C:권장 (Recommended)
  - 일관성을 보장하도록 임의의 선택을 할 수 있음
- D:주의 필요 (Use with Caution)
  - 잠재적 위험 특성을 고려함
### 참고
#### [주의] computed의 반환 값은 변경하지 말 것
* computed의 반환 값은 의존하는 데이터의 파생된 값
* 일종의 snapshot이며 의존하는 데이터가 변경될 때 마다 새 snapshot을 변경하는 것은 의미가 없으므로 계산된 반환 값은 읽기 전용으로 취급되어야 하며 변경되어서는 안됨
* 대신 새 값을 얻기 위해서는 의존하는 데이터를 업데이트 해야 함
#### [주의] computed 사용 시 원본 배열은 변경하지 말 것
* computed에서 reverse() 및 sort() 사용시 원본 배열을 변경하기 때문에 복사본을 만들어서 진행해야 함
```html
return [...numbers].reverse()
```
## Single-File Components
### Single-File Components
#### Component
* 재사용 가능한 코드 블록
#### Component 특징
* UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
* 그러면 자연스럽게 앱은 중첩된 Component의 트리로 구성됨
#### Single-File Components (SFC)
* 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식 (*.vue 파일)
#### SFC파일 예시
* Vue SFC는 HTML, CSS 및 JavaScript 3개를 하나로 합친 것
* template, script 및 style 블록은 하나의 파일에서 컴포넌트의 뷰, 로직 및 스타일을 캡슐화하고 배치
#### SFC 문법 개요
* 각 *.vue 파일은 세 가지 유형의 최상위 언어 블록template, script 및 style으로 구성됨
* 언어 블록의 작성 순서는 상관 없으나 일반적으로 template -> script -> style 순서로 작성
#### 언어 블록 template
* 각 *.vue 파일은 최상위 template 블록을 하나만 포함할 수 있음
#### 언어 블록 script setup
* 각 *.vue 파일을 하나의 script setup 블록만 포함할 수 있음. (일반 script 제외)
* 컴포넌트의 setup() 함수로 사용되어 컴포넌트의 각 인스턴스에 대해 실행
#### 언어 블록 style scope
* *.vue 파일에는 여러 style태그가 포험될 수 있음
* scoped가 지정되면 css는 현재 컴포넌트에만 적용
### SFC build tool (Vite)
#### Vite
* 프론트 엔드 개발 도구
  - 빠른 개발 환경을 위한 빌드 도구와 개발 서버를 제공
#### Vite 튜토리얼
* vue document - 문서 - 시작하기 참고
#### Node Package Manager (NPM)
* Node.js의 기본 패키지 관리자
#### Node.js의 영향
* 기존에 브라우저 안에서만 동작할 수 있었던 JavaScript를 브라우저가 아닌 서버 측에서도 실행할 수 있게 함
  - 프론트엔드와 백엔드에서 동일한 언어로 개발할 수 있게 됨
* NPM을 활용해 수많은 오픈소스 패키지와 라이브러리를 제공하여 개발자들이 손쉽게 코드를 공유하고 재사용할 수 있게 함
#### node_modules
* node.js 프로젝트에서 사용되는 외부 패키지들이 저장되는 디렉토리
* 프로젝트의 의존성 모듈을 저장하고 관리하는 공간
* 프로젝트가 실행될 때 필요한 라이브러리와 패키지들을 포함
* .gitignore에 작성됨
#### pacage-lock.json
* 패키지들의 실제 설치 버전, 의존성 관계, 하위 패키지 등을 포함하여 패키지 설치에 필요한 모든 정보를 포함
* 패키지들의 정확한 버전을 보장하여, 여러 개발자가 협업하거나 서버 환경에서 일관성 있는 의존성을 유지하는 데 도움을 줌
* npm install 명령을 통해 패키지를 설치할 때, 명시된 버전과 의존성을 기반으로 설치
#### package.json
* 프로젝트의 메타 정보와 의존성 패키지 목록을 포함
* 프로젝트의 이름, 버전, 작성자, 라이센스 등과 같은 메타 정보를 정의
  - package-lock.json과 함께 프로젝트의 의존성을 관리하고, 버전 충돌 및 일관성을 유지하는 역할
#### public 디렉토리
* 주로 다음 정적 파일을 위치 시킴
  - 소스코드에서 참조되지 않는
  - 항상 같은 이름을 갖는
  - import 할 필요 없는
* 항상 root 절대 경로를 사용하여 참조
  - public/icon.png는 소스코드에서 /icon.png로 참조 할 수 있음
#### src 디렉토리
* 프로젝트의 주요 소스 코드를 포함하는 곳
* 컴포넌트, 스타일, 라우팅 등 프로젝트의 핵심 코드를 관리
#### src/assets
* 프로젝트 내에서 사용되는 자원(이미지, 폰트, 스타일 시트 등)을 관리
* 컴포넌트 자체에서 참조하는 내부 파일을 저장하는 데 사용
* 컴포넌트가 아닌 곳에서는 public 디렉토리에 위치한 파일을 사용
#### src/components
* Vue 컴포넌트들을 작성하는 곳
#### src/App.vue
* Vue 앱의 최상위 Root 컴포넌트
* 다른 하위 컴포넌트들을 포함
* 애플리케이션 전체의 레이아웃과 공통적인 요소를 정의
#### src/main.js
* Vue 인스턴스를 생성하고, 애플리케이션을 초기화하는 역할
* 필요한 라이브러리를 import 하고 전역 설정을 수행
#### index.html
* Vue 앱의 기본 HTML 파일
* 앱의 진입점 (entry point)
* Root 컴포넌트인 App.vue가 해당 페이지에 마운트 됨
  - Vue 앱이 SPA인 이유
*필요한 스타일 시트, 스트립트 등의 외부 리소스를 로드 할 수 있음(ex. bootstrap CDN)
#### Module
* 프로그램을 구성하는 독립적인 코드 블록 (*.js 파일)
* 개발하는 애플리케이션의 크기가 커지고 복잡해지면서 파일 하나에 모든 기능을 담기가 어려워 짐
* 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이 모듈 즉, js 파일 하나가 하나의 모듈
* 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈간의 문제인지 파악하기 어려워 짐
* 복잡하고 깊은 모듈의 의존성 문제를 해결하기 위한 도구가 필요
  - Bundler
#### Bundler
* 여러 모듈과 파일을 하나(혹은 여러개)의 번들로 묶어 최적화하여 애플리케이션에서 사용할 수 있게 만들어주는 도구
#### Bundler 역할
* 의존성 관리, 코드 최적화, 리소스 관리 등
* Bundler가 하는 작업을 Bundling이라 함
* Vite는 Rollup이라는 Bundler를 사용하며 개발자가 별도로 기타 환경설정에 신경 쓰지 않도록 모두 설정해두고 있음
### Vue Component
#### 컴포넌트 사용 2단계
1. 컴포넌트 파일 생성
2. 컴포넌트 등록 (import)
#### 사전준비
1. 초기에 생성된 모든 컴포넌트 삭제 (App.vue 제외)
2. App.vue 코드 초기화
#### 1. 컴포넌트 파일 생성 and 컴포넌트 파일 등록
* App(부모) - MyComponents(자식) 관계 형성
* **@-'src/'** 경로를 뜻하는 약어
```vue
<template>
  <div>
    <h1>App.vue</h1>
    <MyComponents />
  </div>
</template>

<script setup>
// import MyComponents from './components/MyComponents.vue';
import MyComponents from '@/components/MyComponents.vue';
</script>

<style scoped>

</style>
```
### 추가 주제
#### Virtual DOM
* 가상의 DOM을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념
* 실제 DOM과의 변경 사항 비교를 통해 변경된 부분만 실제 DOM에 적용하는 방식
* 웹 애플리케이션의 성능을 향상시키기 위한 Vue의 내부 렌더링 기술
#### Virtual DOM 패턴의 장점
* 효율성
  - 실제 DOM 조작을 최소화하고, 변경된 부분만 업데이트하여 성능을 향상
* 반응성
  - 데이터의 변경을 감지하고, Virtual DOM을 효율적으로 갱신하여 UI를 자동으로 업데이트
* 추상화
  - 개발자는 실제 DOM 조작을 Vue에게 맡기고 컴포넌트와 템플릿을 활용하는 추상화된 프로그래밍 방식으로 원하는 UI구조를 구성하고 관리할 수 있음
#### Virtual DOM 주의사항
* 실제 DOM에 직접 접근하지 말것
  - JavaScript에서 사용하는 DOM 접근 관련 메서드 사용 금지
  - querySelector, createElement, addEventListener 등
* Vue의 ref와 Lifecycle Hooks 함수를 사용해 간접적으로 접근하여 조작할 것
#### 직접 DOM 엘리먼트에 접근해야 하는 경우
* ref 속성을 사용하여 특정 DOM 엘리먼트에 직접적인 참조를 얻을 수 있음
```vue
<template>
  <div>
    <h1>App.vue</h1>
    <input ref='input'>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 변수명은 템플릿 ref 값과 일치해야 함
const input = ref(null)

onMounted(() => {
  console.log(input.value)
})
</script>

<style scoped>

</style>
```
### 참고
#### Scaffolding (스캐폴딩)
* 새로운 프로젝트나 모듈을 시작하기 위해 초기 구조와 기본 코드를 자동으로 생성하는 과정
* 개발자들이 프로젝트를 시작하는 데 도움을 주는 틀이나 기반을 제공하는 작업
* 초기 설정, 폴더 구조, 파일 템플릿, 기본 코드 등을 자동으로 생성하여 개발자가 시작할 때 시간과 노력을 절약하고 일관된 구조를 유지할 수 있도록 도와줌
## Component State Flow
### Passing Props
#### 같은 데이터 하지만 다른 컴포넌트
* 동일한 사진 데이터가 한 화면에 다양한 위치에서 여러번 출력되고 있음
* 하지만 해당 페이지를 구성하는 컴포넌트가 여러 개라면 각 컴포넌트가 개별적으로 동일한 데이터를 관리해야 할까?
* 그렇다면 사진을 변경 해야 할 때 모든 컴포넌트에 대해 변경 요청을 해야함
* **공통된 부모 컴포넌트에서 관리하자**
* 부모는 자식에게 데이터를 전달 (pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)
#### Props
* 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성
#### One-Way Data Flow
모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성(one-way-down binding)
#### Propt 특징
* 부모 속성이 업데이트되면 자식으로 흐르지만 그 반대는 안됨
* 즉, 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며 불가능
* 또한 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 props가 최신 값으로 업데이트 됨
* **부모 컴포넌트에서만 변경하고 이를 내려 받는 자식 컴포넌트는 자연스럽게 갱신**
#### 단방향인 이유
* 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 병경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위해
#### Props 선언
* 부모 컴포넌트에서 보낸 Props를 사용하기 위해서는 자식 컴포넌트에서 명시적인 props 선언이 필요
* 부모 컴포넌트 Parent에서 자식 컴포넌트 ParentChild에 보낼 Props 작성
```vue
<!-- 추가 작성하는 거 없이 이것만 작성 -->
<template>
    <div>
        <ParentChild my-msg="message" />
    </div>
</template>
```
#### Props 선언 2가지 방법
1. 문자열 배열을 사용한 선언
2. 객체를 사용한 선언
#### 문자열 배열을 사용한 선언
* defineProps()를 사용하여 props를 선언
```vue
<template>
    <div>
        {{ myMsg }}
    </div>
</template>

<script setup>
defineProps([myMsg])
</script>
```
#### 객체를 사용한 선언
* 객체 선언 문법의 각 객체 속성의 키는 props의 이름이 되며, 객체 속성의 값은 값이 될 데이터의 타입에 해당하는 생성자 함수(Number, String...)여야 함
* **객체 선언 문법 사용 권장**
```vue
<template>
    <div>
        {{ myMsg }}
    </div>
</template>

<script setup>
defineProps({
    myMsg: String,
    }
)
</script>
```
#### prop 데이터 사용
* 템플릿에서 반응형 변수와 같은 방식으로 활용
* props를 객체로 반환하므로 필요한 경우 JavaScript에서 접근 가능
```vue
<script setup>
  const props = defineProps({ myMsg: String })
</script>
```
#### Props 한단계 더 내려보내기
* 위와 동일
#### Props 세부사항
1. Props Name Casing (Props 이름 컨벤션)
2. Static Props & Dynamic Props
#### Props Name Casing
* 선언 및 템플릿 참조 시 (->camelCase)
```vue
<div>{{ myMsg }}</div>
<script setup>
  const props = defineProps({ myMsg: String })
</script>
```
* 자식 컨포넌트로 전달 시 (-> kebap-case)
```vue
<ParentGrandChild :my-msg="myMsg" />
```
* **기술적으로는 카멜케이스도 가능하나 HTML속성 표기법과 동일하게 케밥케이스로 표기할 것을 권장**
#### Static Props & Dynamic Props
* 지금까지 작성한 것은 Static(정적) props
* v-bind를 사용하여 **동적으로 할당된 props**를 사용할 수 있음
```vue
<ParentChild my-msg="message" :dynamic-props="name"/>

<script setup>
import { ref } from 'vue'

const name = ref('Alice')
</script>

<!-- ParentChild.vue -->
<script setup>
defineProps({
    myMsg: String,
    dynamicProps: String})
</script>
```
### Component Events
#### 자식의 데이터를 변경할때 부모의 데이터도 변경하고 싶다면
* 부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event) **부모가 prop 데이터를 변경하도록 소리쳐야 한다.**
#### $emit()
* 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
  - '$'표기는 Vue 인스턴스나 컴포넌트 내에서 제공되는 전역 속성이나 메서드를 식별하기 위한 접두어
#### 이벤트 발신 및 수신(Emitting and Listening to Events)
* $emit을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트를 발신
```html
<button @click="$emit('someEvent')">클릭</button>
```
* 그러면 부모는 v-on을 사용하여 수신할 수 있음
```vue
<ParentComp @some-event="someCallback" />
```
#### 이벤트 발신 및 수신하기
* ParentChild에서 someEvent라는 이름의 사용자 정의 이벤트를 발신
```html
<!-- 자식에서 이벤트를 보냄 -->
<button @click="$emit('someEvent')">클릭</button>

<!-- 부모가 자식의 이벤트를 받음 -->
<template>
    <div>
        <ParentChild @some-event="someCallback" my-msg="message" :dynamic-props="name"/>
    </div>
</template>

<script setup>
const someCallback = function () {
    console.log('Parentchild가 발신한 이벤트를 수신했어요')
}
</script>
```
#### emit 이벤트 선언
* defineEmits()를 사용하여 명시적으로 발신할 이벤트를 선언할 수 있음
* script에서 $emit 메서드를 접근할 수 없기 때문에 defineEmits()는 $emit 대신 사용할 수 있는 동등한 함수를 반환
## Router
### Routing
#### Routing
* 네트워크에서 경로를 선택하는 프로세스
  - 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술
### Vue Router
#### Vue Router
* vue 공식 라우터 (The official Router for Vue.js)
#### views
* RoutView 위치에 렌더링 할 컴포넌트를 배치
* 기존 components 폴더와 기능적으로 다른 것은 없으며 단순 분류의 의미로 구성됨
  - **일반 컴포넌트와 구분하기 위해 컴포넌트 이름을 View로 끝나도록 작성하는 것을 권장**
#### 라우팅 기본
* index.js에 라우터 관련 설정 작성(주소, 이름, 컴포넌트)
* RoutLink의 'to' 속성으로 index.js에서 정의한 주소 속성 값(path)을 사용
#### Named Routes : index.js에서 정해진 이름을 사용하는 법
* 경로에 이름을 지정하는 라우팅
* 경로에 연결하려면 RouterLink에 v-bind를 사용해 'to' prop 객체로 전달
```html
<RouterLink :to="{ name:'home' }">Home</RouterLink>
<RouterLink :to="{ name:'about' }">About</RouterLink>
```
#### Named Routes 장점
* 하드 코딩 된 URL을 사용하지 않아도 됨
* URL 입력 시 오타 방지
### Dynamic Route Matching with Params
#### 매개 변수를 사용한 동적 경로 매칭
* 주어진 패턴 경로를 동일한 컴포넌트에 매핑 해야 하는 경우 활용
* 예를 들어 모든 사용자의 ID를 활용하여 프로필 페이지 url을 설계 한다면?
  - user/1
  - user/2
  - user/3
    - 일정한 패턴의 url작성을 반복해야함
#### 매개 변수를 사용한 동적 경로 매칭 : index.js
* UserView 컴포넌트 라우트 등록
* 매개변수는 콜론(:)으로 표기
```javascript
{
  path: '/user/:id', 
  name: 'user',
  component: userView
}
```
#### 매개 변수를 컴포넌트에서 사용하는 법
* 라우트의 매개변수는 컴포넌트에서 $route.params로 참조 가능
```html
<h2>{{ $route.params.id }}번 유저의 페이지입니다.</h2>
```
#### 매개 변수를 컴포넌트의 스크립트에서 사용하는 법
```javascript
<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router';

const route = useRoute()
const userId = ref(route.params.id)
</script>
```
### Programmatic Navigation
#### 프로그래밍 방식 네비게이션
* router의 인스턴스 메서드를 사용해 RouterLink로 a태그를 만드는 것처럼 프로그래밍으로 네비게이션 관련 작업을 수행할 수 있음
* 다른 위치로 이동하기
  - router.push()
* 현재 위치 바꾸기
  - router.replace()
#### router.push()
* 다른 url로 이동하는 메서드
* 새 항목을 history stack에 push하므로 사용자가 브라우저 뒤로 가기 버튼을 클릭하면 이전 url로 이동할 수 있음
* RouterLink를 클릭했을때 내부적으로 호출되는 메서드 이므로 RouterLink를 클릭하는 것은 route.push()를 호출하는 것과 같음
  - 선언적 : \<RouterLink : to='...'>\
  - 프로그래밍적 : router.push(...)
```javascript
import { useRoute, useRouter } from 'vue-router';

const goHome = function() {
    router.push({ name:'home' })
}
```
* 버튼 클릭으로 보내주면 됨 : 뒤로가기가 됨
#### router.replace()
* 현재 위치 바꾸기
* push 메서드와 달리 다른 url로 이동한뒤 뒤로가기 불가능
  - 선언적 : \<RouterLink : to='...' replace>\
  - 프로그래밍적 : router.replace(...)
### Navigation Guard
#### Navigation Guard
* Vue router를 통해 특정 url에 접근할 때 다른 url로 redirect를 하거나 취소하여 네비게이션을 보호
  - ex) 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함
#### Navigation Guard 종류
* Globally (전역 가드)
  - 애플리케이션 전역에서 동작
  - index.js에서 정의
* Per-route (라우터 가드)
  - 특정 route에서만 동작
  - index.js의 각 routes에 정의
* In-component (컴포넌트 가드)
  - 특정 컴포넌트 내에서만 동작
  - 컴포넌트 script에 정의
### Globally Guard
#### router.beforeEach()
* 다른 url로 이동하기 직전에 실행되는 함수
```javascript
router.beforeEach((to, from) => {
  ...
  return false
})
```
* to : 이동 할 url 정보가 담긴 Route 객체
* from : 현재 url 정보가 담긴 Route 객체
* 선택적 반환(return) 값
  1. false
  2. Route Location
* false
  - 현재 내비게이션을 취소
* Route Location
  - router.push()를 호출하는 것처럼 경로 위치를 전달하여 다른 위치로 redirect
    - **return이 없다면 'to' url Route 객체로 이동**
#### router.beforeEach 예시 : index.js
```javascript
router.beforeEach((to, from) => {
  ...
  return false
})

// index.js에 쓰면 어디서 어디로 가는지 알수 있음
router.beforeEach((to, from) => {
  console.log(to)
  console.log(from)
})
```
#### router.beforeEach를 활용하여 로그인이 되어있지 않으면 진입을 막기
```javascript
// index.js

router.beforeEach((to, from) => {
  console.log(to)
  console.log(from)
  const isAuthenticated = false
  
  if (!isAuthenticated && to.name !== 'login') {
    console.log('로그인이 필요합니다.')
    return { name: 'login'}
  }
})
```
#### router.beforeEnter : 이미 로그인한 상태라면 login페이지 진입을 막고 다른곳으로 이동시키기
```javascript
// index.js

{
  path: '/login', 
  name: 'login',
  component: LoginView,
  beforeEnter: (to, from) => {
    if (isAuthenticated === true) {
      console.log('이미 로그인 되어 있습니다.')
      return { name : 'home' }
    }
  }
}
```
#### onBeforeRouteLeave 활용 : 사용자가 userView를 떠날 시 팝업 창 출력
```javascript
// userView 내부.
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router';
// Inn-component Guard
onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('정말 떠나실 건가요?')
    if (answer === false) {
        return false
    }
})
```
#### onBeforeRouteUpdate 활용 : UserView 페이지에서 다른 id를 가진 User의 페이지로 이동하기
```javascript
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router';
// 2.
const goAnotherUser = function () {
    router.push({name: 'user', params: {id: 100}})
}

onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id
})
```