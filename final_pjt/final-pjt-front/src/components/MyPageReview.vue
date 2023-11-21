<template>
    <div @click="goToDetail(props.mypageToReview.movie)">
        유저 : {{ props.mypageToReview.user }} | 별점 : {{ props.mypageToReview.score }} | {{ props.mypageToReview.content }}
    </div>
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

</style>