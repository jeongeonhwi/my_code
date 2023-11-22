<template>
    <div @click="goToDetail(props.mypageToReview.movie)">
        <span v-if="props.mypageToReview.score === 0">&#10032;&#10032;&#10032;&#10032;&#10032; </span>
        <span v-if="props.mypageToReview.score === 1">★&#10032;&#10032;&#10032;&#10032; </span>
        <span v-if="props.mypageToReview.score === 2">★★&#10032;&#10032;&#10032; </span>
        <span v-if="props.mypageToReview.score === 3">★★★&#10032;&#10032; </span>
        <span v-if="props.mypageToReview.score === 4">★★★★&#10032; </span>
        <span v-if="props.mypageToReview.score === 5">★★★★★ </span>
        <span class="fs-6">{{ props.mypageToReview.score }}</span>
        <p class="m-1 ms-2">{{ props.mypageToReview.content }}</p>
        <span class="review-color">
            {{ props.mypageToReview.updated_at.slice(0,10) }}.
            {{ props.mypageToReview.updated_at.slice(11, 16) }}&nbsp;
        </span>
    </div>
    <hr>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
    mypageToReview:Object,
})

const goToDetail = function (movieId) {
    router.push({name:'movieDetail', params: {movie_pk:movieId}})
}
</script>

<style scoped>
.review-color {
    color: #aaa9a9;
}
</style>