<template>
    <div>
        <h1>상품 목록 페이지</h1>
        <ProductDetail
        v-for="product in store.productList"
        :productView-to-productDetail="product"
        />
    </div>
  </template>
  
  <script setup>
  import { productListStore } from '@/stores/products';
  import ProductDetail from '../components/ProductDetail.vue';

  const store = productListStore()
  </script>
  
  <style scoped>
  
  </style>