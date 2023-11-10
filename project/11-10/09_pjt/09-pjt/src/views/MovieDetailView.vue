<template>
    <div class="movie-card">
        <h1>영화 상세 정보 페이지</h1>
        <div v-if="movie.poster_path"> 
                <img :src="'https://image.tmdb.org/t/p/original'+movie.poster_path" alt="#">
            </div>
            <h2>{{ movie.title }}</h2>
            <div>
                상세설명 : {{ movie.overview }}
            </div>
            <button @click="goToDetail(movie)">자세히보기</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'

const route = useRoute()
const movie = ref('')
const movieId = route.params.movieId
const tmdbApi = '8705447c756fa62d8c95f823e7d9660c'

const movieURL = `https://api.themoviedb.org/3/movie/${movieId}?api_key=${tmdbApi}`

axios.get(movieURL)
    .then((response) => {
        movie.value = response.data
        console.log(response)
    }).catch((error) => {
        console.log(error)
    })

</script>

<style scoped>

</style>