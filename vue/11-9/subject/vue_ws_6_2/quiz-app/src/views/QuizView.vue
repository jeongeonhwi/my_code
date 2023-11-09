<template>
    <h1>퀴즈뷰</h1>
    <div v-for="quiz, index in quizList" :key="quiz.id">
        <p class="jb-bold">{{ quizList.length - index }}{{ quiz.question }}</p>
        <p>정답 입력</p>
        <p><input type="text" class="fullSize" ></p>
    </div>
</template>

<script setup>
import { ref } from 'vue'


const props = defineProps({
    quizInfo:Object,
})


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