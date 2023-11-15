<template>
  <div>
      <h1>Login</h1>
      <form @submit.prevent="logIn">
        <input type="text" v-model.trim="userName">
        <input type="password" v-model.trim="password">
        <input type="submit">
      </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const userName = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username : userName.value,
    password : password.value
  }
  store.logIn(payload)
}
</script>

<style>

</style>
