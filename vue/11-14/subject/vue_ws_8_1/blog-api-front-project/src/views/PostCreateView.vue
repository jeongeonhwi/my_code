<template>
    <div>
        <h1>게시글 생성 페이지</h1>
        <form @submit.prevent="createPost">
            <p>카테고리 선택:</p>
            <select v-model="category">
                <option :value="category.name" v-for="category in categoryListValue">{{ category.name }}</option>
            </select>
            <p>제목:</p>
            <input type="text" v-model="title">
            <p>내용:</p>
            <textarea cols="30" rows="5" v-model="content"></textarea>
            <p><input type="submit" value="게시글 생성"></p>
        </form>
    </div>
</template>

<script setup>
import { usePostStore } from '@/stores/posts'
import { onMounted, computed, ref } from 'vue';
import axios from 'axios'
import router from '../router';

const store = usePostStore()
const category = ref('')
const title = ref('')
const content = ref('')
onMounted(() => {
    store.getCategoryList()
})

const categoryListValue = computed(() => {
    return store.categoryListValue
})

const createPost = function() {
    axios({
        method:'post',
        url:'http://127.0.0.1:8000/api/v1/posts/',
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