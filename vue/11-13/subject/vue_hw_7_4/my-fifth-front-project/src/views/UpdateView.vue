<template>
    <div>
      <h2>데이터 수정 페이지</h2>
      <p>
        {{ user.name }}
      </p>
      <p>
        {{ user.balance }}
      </p>
      <button @click="updateBalance">+</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRoute, useRouter } from 'vue-router';
  import { useBalanceStore } from '../stores/balance';

  const route = useRoute()
  const userName = ref(route.params.name)
  const store = useBalanceStore()
  const user = store.getUserByName(userName.value)
  
  const updateBalance = function () {
    store.updateBalance(userName.value)
  }
  </script>
  
  <style scoped>
  
  </style>