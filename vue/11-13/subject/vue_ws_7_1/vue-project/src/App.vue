<template>
  <div>
    <RouterLink :to="{name:'home'}">home</RouterLink> / 
    <RouterLink :to="{name:'products'}">products</RouterLink> / 
    <RouterLink :to="{name:'favorite'}">favorite</RouterLink> / 

    <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

</style>