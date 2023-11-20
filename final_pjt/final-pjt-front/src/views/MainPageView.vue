<template>
    <div >
        <h1>최신개봉영화</h1>
        <!-- <p>{{ movies }}</p> -->
            <MovieDetail
            v-for="movie in movies"
            :key="movie.id"
            :main-to-detail="movie"
            />
        
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import MovieDetail from '@/components/MovieDetail.vue'
import axios from 'axios';

const store = useCounterStore()
const movies = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/movies/`
    })
        .then((res) => {
            movies.value = res.data
            // console.log(movies.value)
        })
        .catch((err) => {
            console.log(err)
        })
})
</script>

<style scoped>

</style>