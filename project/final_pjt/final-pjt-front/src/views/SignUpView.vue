<template>
    <div class="sign-up-box d-flex flex-column align-items-center mt-5">
        <!--회원가입 입력사항좀 추가하기-->
        <h1>회원가입</h1>
        <form @submit.prevent="signUp">
            <div class="form-group mt-5">
                <label for="username">아이디  </label>
                <input type="text" id="username" v-model.trim="username">
            </div>

            <div class="form-group">
                <label for="password1">비밀번호  </label>
                <input type="password" id="password1" v-model.trim="password1">
            </div>

            <div class="form-group">
                <label for="password2">비밀번호 확인 </label>
                <input type="password" id="password2" v-model.trim="password2">
            </div>

            <div class="d-flex flex-column align-items-center mt-3">
                <input type="submit" value="회원가입">
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
    const payload = {
        username: username.value,
        password1: password1.value,
        password2: password2.value
    }
    store.signup(payload)
}



</script>

<style scoped>
.sign-up-box {
    width: 400px;
    height: 400px;
    border: 2px solid white;
    margin: 0 auto;
}

.form-group {
  margin-bottom: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
</style>