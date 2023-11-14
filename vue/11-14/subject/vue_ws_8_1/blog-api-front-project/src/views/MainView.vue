<template>
    <div class="h-600 d-flex flex-column justify-content-center align-items-center">
        <h1>ㅇㅇ이의 블로그 </h1>
        <p>welcome to my personal blog!</p>
        <p v-for="category in categoryListValue">{{ category.name }}</p>
    </div>
</template>

<script setup>
import { usePostStore } from '@/stores/posts'
import { onMounted, computed } from 'vue';

const store = usePostStore()

onMounted(() => {
    store.getCategoryList()
})

const categoryListValue = computed(() => {
    return store.categoryListValue
})
</script>

<style scoped>
.h-600 {
    height: 600px;
}
</style>