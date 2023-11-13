<template>
    <div>
        <h1>pinia 연습하기</h1>
        <div class="box box-color">
            <ParentPage 
            v-for="family in store.familyInfo"
            :my-msg="family"
            />
        </div>
    </div>
  </template>
  
  <script setup>
import { useFamilyStore } from '@/stores/family'
import ParentPage from './ParentPage.vue';

const store = useFamilyStore()
  </script>
  <style scoped>
  .box-color {
   background-color: rgb(241, 243, 245);   
  }
  </style>
<style>
.box {
    border: 1px solid rgb(214, 209, 209);
}
</style>