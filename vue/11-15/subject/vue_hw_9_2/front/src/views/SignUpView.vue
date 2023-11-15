<template>
    <div>
        <h1>회원가입</h1>
        <form @submit.prevent="signUp">
            <label for="username">username : </label>
            <input type="text" v-model.trim="userName"><br>

            <label for="password1">password : </label>
            <input type="password" v-model.trim="password1"><br>

            <label for="password2">password comfirmation : </label>
            <input type="password" v-model.trim="password2">

            <input type="submit" value="SignUp">
        </form>
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { ref, computed } from 'vue'

const store = useArticleStore()
const userName = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
    const payload = {
        username : userName.value,
        password1: password1.value,
        password2: password2.value
    }
    // console.log(payload)
    store.signUp(payload)
}
</script>

<style scoped>

</style>