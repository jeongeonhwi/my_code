<template>
    <div @click="goToDetailView(props.mainToDetail.id)">
        <img :src="`https://image.tmdb.org/t/p/w200${props.mainToDetail.poster_path}`" alt="poster_path">
        {{ props.mainToDetail.id }}
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
    mainToDetail:Object
})

const goToDetailView = function(moviePk) {
    router.push({name:'movieDetail', params: {movie_pk:moviePk}})
}
</script>

<style scoped>

</style>