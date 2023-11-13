<template>
  <div>
    <RouterLink :to="{name:'home'}">home</RouterLink> / 
    <RouterLink :to="{name:'products'}">products</RouterLink> / 
    <RouterLink :to="{name:'favorite'}">favorite</RouterLink> 
    <span v-show="store.countFavorite"> {{ store.countFavorite }}</span>

    <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { productListStore } from '@/stores/products';

const store = productListStore()
</script>

<style scoped>

</style>