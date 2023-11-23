<template>
    <div class="login-box d-flex flex-column align-items-center mt-5">
        <h1>로그인</h1>
        <form @submit.prevent="logIn">
            <div class="form-group mt-5">
                <label for="username">아이디</label>
                <input type="text" id="username" v-model.trim="username"><br>
            </div>

            <div class="form-group">
                <label for="password">비밀번호</label>
                <input type="password" id="password" v-model.trim="password"><br>
            </div>

            <div class="d-flex flex-column align-items-center mt-3">
                <input type="submit" value="확인">
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
    const payload = {
        username: username.value,
        password: password.value
    }
    store.logIn(payload)
}

</script>

<style scoped>
.login-box {
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