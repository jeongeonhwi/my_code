<template>
    <div class="box">
        <h3>
            자식 페이지
        </h3>
        {{ props.parentToChild.name }}
        <br>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    parentToChild:Object,
  })
  </script>
  
  <style scoped>
  div {
    background-color: white;
  }
  </style>