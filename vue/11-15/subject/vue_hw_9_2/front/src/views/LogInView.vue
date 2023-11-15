<template>
    <div>
        <h1>LogIn</h1>
        <form @submit.prevent="logIn">
            <label for="username">username : </label>
            <input type="text" v-model.trim="userName"><br>

            <label for="password">password : </label>
            <input type="password" v-model.trim="password"><br>
            
            <input type="submit" value="login">
        </form>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const userName = ref(null)
const password = ref(null)

const logIn = function () {
    // console.log('!!!!!!!!!!')
    const payload = {
        username:userName.value,
        password:password.value,
    }
    store.logIn(payload)
}
</script>

<style scoped>

</style>