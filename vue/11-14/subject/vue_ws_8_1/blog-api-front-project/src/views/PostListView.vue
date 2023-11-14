<template>
    <div>
        <h1>게시글 목록 페이지</h1>
        <RouterLink :to="{name:'postcreate'}">게시글 생성</RouterLink>
        {{ postListValue }}
    </div>
</template>

<script setup>
import { usePostStore } from '@/stores/posts'
import { onMounted, computed } from 'vue';

const store = usePostStore()

onMounted(() => {
    store.getPostList()
})

const postListValue = computed(() => {
    return store.postListValue
})
</script>

<style scoped>

</style>