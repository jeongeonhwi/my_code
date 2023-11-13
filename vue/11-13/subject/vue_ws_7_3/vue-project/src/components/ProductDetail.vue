<template>
    <div>
        <p>{{ productViewToProductDetail.name }}</p>
        <img :src="productViewToProductDetail.imagePath" alt="">
        <p>\{{ productViewToProductDetail.price }}</p>
        <p v-show="productViewToProductDetail.isFavorite"
        @click="favorite(productViewToProductDetail.name)"
        >찜O</p>
        <p v-show="!productViewToProductDetail.isFavorite"
        @click="favorite(productViewToProductDetail.name)"
        >찜X</p>
    </div>
  </template>
  
  <script setup>
import { productListStore } from '../stores/products';

const props = defineProps({
    productViewToProductDetail:Object,
})
const store = productListStore()

const favorite = function (name) {
  store.favoriteFunction(name)
}
  </script>
  
  <style scoped>
  img {
    width: 200px;
  }
  </style>