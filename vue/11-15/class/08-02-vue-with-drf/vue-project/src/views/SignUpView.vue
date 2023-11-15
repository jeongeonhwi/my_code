<template>
  <div>
    <h1>SignUp</h1>
    <form @submit.prevent="signUp">
      <input type="text" v-model.trim="userName">
      <input type="password" v-model.trim="password1">
      <input type="password" v-model.trim="password2">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const userName = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payload = {
    username: userName.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}
</script>

<style>

</style>
