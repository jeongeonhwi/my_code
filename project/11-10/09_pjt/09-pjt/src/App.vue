<template>
  <div>
    <RouterLink :to="{name:'home'}">home</RouterLink> /
    <RouterLink :to="{name:'movieList'}">movieList</RouterLink> /
    <RouterLink :to="{name:'reviewSearch'}">reviewSearch</RouterLink>
  </div>

<RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>