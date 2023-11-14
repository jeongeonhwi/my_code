<template>
    <div>
        <form @submit.prevent="createCategory">
            <p>Category 종류:</p>
            <input type="text" v-model="categoryText">
            <input type="submit" value="카테고리 생성">
        </form>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import router from '../router';

const categoryText = ref('')

const createCategory = function() {
    axios({
        method:'post',
        url:'http://127.0.0.1:8000/api/v1/category/',
        data:{
            name:categoryText.value
        }
    })
        .then((res) => {
            // console.log(res.data)
            router.push({name:'home'})
        })
        .catch((error) => {
            console.log(error)
        })
}
</script>

<style scoped>

</style>