<template>
    <div>
        <p>{{ productViewToProductDetail.name }}</p>
        <img :src="productViewToProductDetail.imagePath" alt="">
        <p>\{{ productViewToProductDetail.price }}</p>
        <p v-show="productViewToProductDetail.isFavorite">찜O</p>
        <p v-show="!productViewToProductDetail.isFavorite">찜X</p>
    </div>
  </template>
  
  <script setup>
const props = defineProps({
    productViewToProductDetail:Object,
})
  </script>
  
  <style scoped>
  img {
    width: 200px;
  }
  </style>