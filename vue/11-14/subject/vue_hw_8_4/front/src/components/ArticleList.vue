<template>
  <div v-for="article, index in store.articles">
    <h4>{{ index+1 }}번 게시글</h4>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <hr>
  </div>
  <ul>
    <li @click="goToCreatePage">게시글 생성 페이지</li>
  </ul>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const router = useRouter()

onMounted(() => {
  store.getArticles()
})

const goToCreatePage = function () {
  router.push({name:'create'})
}
</script>

<style lang="scss" scoped>

</style>