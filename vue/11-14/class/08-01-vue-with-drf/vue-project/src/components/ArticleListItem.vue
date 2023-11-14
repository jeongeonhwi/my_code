<template>
  <div>
    <h5>{{ props.article.id }}</h5>
    <p>{{ props.article.title }}</p>
    <p>{{ props.article.content }}</p>
    <RouterLink :to="{name:'DetailView', params: {id:props.article.id}}">
      [Detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const props = defineProps({
  article: Object,
})
</script>
