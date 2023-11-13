<template>
    <div>
      <p>{{ mainViewToMainPage.name }}</p>
      <p>{{ mainViewToMainPage.balance }}</p>
      <button @click="updateBalance(mainViewToMainPage)">updateBalance</button>
    </div>
  </template>
  
  <script setup>
import { useRoute, useRouter } from 'vue-router';
// import { routeLocationKey } from 'vue-router';

  const props = defineProps({
    mainViewToMainPage:Object
  })

  const router = useRouter()
  const updateBalance = function (mainViewToMainPage) {
    router.push({name:'update', params: {name:mainViewToMainPage.name}})
  }
  </script>
  
  <style scoped>
  
  </style>