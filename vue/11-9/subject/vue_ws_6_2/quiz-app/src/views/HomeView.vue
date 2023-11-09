<template>
    <div>
        <br>
            <h2>퀴즈 앱 사용 방법</h2>
            <br>
            <h1>1. 퀴즈 목록 확인하기</h1>
            <p>퀴즈 목록 페이지에서 다양한 퀴즈를 확인하세요.</p>
        <br>
        <br>
        <QuizView :quiz-info="quizList" />
        <br>
        <br>
            <h1>2. 퀴즈 생성하기</h1>
            <p>퀴즈는 직접 생성 할 수도 있어요.</p>
            <div>
                <div>
                    <br>
                    <p class="fontSizeUp">퀴즈 생성</p>
                    <br>
                    <p>문제</p>
                    <input type="text" class="fullSize" v-model="inputQuest">
                    <p>답안</p>
                    <input type="text" class="fullSize" v-model="inputCorrect">
                    <br>
                    <br>
                    <button class="fullSize btn btn-primary" @click="createEvent">퀴즈 생성</button>
                </div>
            </div>
        <br>
        <br>
            <h1>3. 정답 페이지</h1>
            <p>작성한 답안이 정답인지 확인하세요.</p>
            <div v-for="quiz, index in quizList">
                <div>
                    <p>{{ quizList.length - index }}번 문제</p>
                    <p class="fontSizeUp">정답 확인</p>
                    <div>
                        <h4>정답입니다!</h4>
                        <p>나의 제출 답안: {{ inputCheckQuest }}</p>
                        <p>정답: {{ quiz.correct }}</p>
                    </div>
                </div>
            </div>
    </div>
    <!-- <p>{{ inputCheckQuest }}</p>
    <input type="text" v-model="inputCheckQuest"> -->
</template>

<script setup>
import { ref } from 'vue'
import QuizView from '@/views/QuizView.vue'

const inputCheckQuest = ref('')

const inputQuest = ref('')
const inputCorrect = ref('')
let id = 0

const createEvent = function() {
    if (inputQuest.value || inputCorrect.value) {
        quizList.value.push({id:id++, 'question':inputQuest.value, 'correct':inputCorrect.value})
        inputCorrect.value = ''
        inputQuest.value = ''
    }
}
const quizList = ref([
    {id:id++, question:'번 문제. 웹 애플리케이션을 개발할 때, 사용자의 브라우저에서 보여지는 부분을 렌더링하는 언어는 무엇인가요?',
    correct:'html'
    },
    {id:id++, question:'번 문제. Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?',
    correct:'venv'
    },
    {id:id++, question:'번 문제. 웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?',
    correct:'api'
    },
    {id:id++, question:'번 문제. HTML에서 텍스트 입력란을 만드는 데 사용되는 요소는?',
    correct:'input'
    },
    {id:id++, question:'번 문제. 웹 애플리케이션을 개발할 때, 사용자의 브라우저에서 보여지는 부분을 렌더링하는 언어는 무엇인가요?',
    correct:'html'
    },
])
</script>

<style scoped>
p {
    margin: 0px;
}

div {
    padding-left: 10px;
}

.fullSize {
    width: 95%;
}

.jb-bold {
        font-weight: bold;
      }

.fontSizeUp {
    font-size: x-large;
    font-weight: bold;
}
</style>