<template>
  <div>
    <nav>
      <RouterLink :to="{ name: 'main' }">Home</RouterLink> /
      <RouterLink :to="{ name: 'SignUpView' }" v-if="!store.isLogin">회원가입 /</RouterLink>
      <RouterLink :to="{ name: 'LogInView' }" v-if="!store.isLogin"> 로그인 / </RouterLink>
      <span @click="store.logOut" v-if="store.isLogin">로그아웃 / </span>
      <RouterLink :to="{ name: 'RecommendMovieView' }">추천 영화</RouterLink> / 
      <RouterLink :to="{ name: 'popularActors' }">인기배우</RouterLink>
    </nav>

  </div>
  <h2 v-if="store.isLogin">{{ store.showUsername }}님 환영합니다</h2>
  <RouterView />
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterView, RouterLink } from 'vue-router'


const store = useCounterStore()
</script>

<style scoped>

</style>