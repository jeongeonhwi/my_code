<template>
    <div>
        <!--회원가입 입력사항좀 추가하기-->
        <h1>회원가입</h1>
        <form @submit.prevent="signUp">
            <label for="username">아이디 : </label>
            <input type="text" id="username" v-model.trim="username"><br>

            <label for="password1">비밀번호 : </label>
            <input type="password" id="password1" v-model.trim="password1"><br>

            <label for="password2">비밀번호 확인 : </label>
            <input type="password" id="password2" v-model.trim="password2">

            <input type="submit" value="회원가입">
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

</style>