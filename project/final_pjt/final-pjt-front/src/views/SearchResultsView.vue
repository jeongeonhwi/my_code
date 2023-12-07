<template>
    <div>
      <h2>검색 결과</h2>
      <ul>
        <li v-for="video in store.state.searchResults" :key="video.id.videoId">
          <iframe :src="'https://www.youtube.com/embed/' + video.id.videoId" width="560" height="315" frameborder="0" allowfullscreen></iframe>
          <p>{{ video.snippet.title }}</p>
          <p>{{ video.snippet.description }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter';
  
  const store = useCounterStore();
  </script>
  
  <style scoped>
  /* Add styling if needed */
  </style>