<template>
    <div >
        <h1>최신개봉영화</h1>
            <MovieDetail
            v-for="movie in movie_list"
            :key="movie.pk"
            :main-to-detail="movie"
            />
        
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import MovieDetail from '@/components/MovieDetail.vue'

const store = useCounterStore()
const movie_list = store.movieList


</script>

<style scoped>

</style>