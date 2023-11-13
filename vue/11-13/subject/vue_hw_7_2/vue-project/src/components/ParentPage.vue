<template>
    <div>
        <h2>
            부모 컴포넌트
        </h2>
        <p>{{ props.myMsg.father }}</p>
        <p>{{ props.myMsg.mother }}</p>
        <ChildPage
        v-for="children in props.myMsg.children"
        :parent-to-child="children"
        />
    </div>
  </template>
  
  <script setup>
  import ChildPage from './ChildPage.vue';
const props = defineProps({
    myMsg:Object,
})
  </script>
  
  <style scoped>
  
  </style>