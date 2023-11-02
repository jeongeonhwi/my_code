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