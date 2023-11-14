<template>
    <div>
        <h1>게시글 생성 페이지</h1>
        <form @submit.prevent="createArticle">
            <label for="title">제목 : </label>
            <input type="text" id="title" v-model="title">
            <label for="content">내용 : </label>
            <input type="text" id="content" v-model="content">
            <input type="submit">
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router';
import axios from 'axios'
import router from '../router';

const store = useArticleStore()
const title = ref('')
const content = ref('')

const createArticle = function() {
    axios({
        method:'post',
        url: 'http://127.0.0.1:8000/api/v1/articles/',
        data:{
            title:title.value,
            content:content.value
        }
    })
        .then((res) => {
            router.push({name:'home'})
        })
    }
</script>

<style scoped>

</style>