<template>
    <div @click="goToDetailView(props.mainToDetail.pk)">
        <img :src="`https://image.tmdb.org/t/p/w200${props.mainToDetail.fields.poster_path}`" alt="poster_path">
        {{ props.mainToDetail.pk }}
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