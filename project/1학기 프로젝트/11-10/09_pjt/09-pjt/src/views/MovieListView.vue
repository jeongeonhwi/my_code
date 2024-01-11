<template>
    <div>
        <h1>전체 영화 목록 페이지</h1>
        <!-- {{ movieList }} -->
        
        <div v-for="movie in movieList" class="movie-card">
            <div v-if="movie.poster_path"> 
                <img :src="'https://image.tmdb.org/t/p/original'+movie.poster_path" alt="#">
            </div>
            <h2>{{ movie.title }}</h2>
            <div>
                상세설명 : {{ movie.overview }}
            </div>
            <button @click="goToDetail(movie)">자세히보기</button>
        </div>
        
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const router = useRouter()

const tmdbApi = '8705447c756fa62d8c95f823e7d9660c'

const tmdbURL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=vote_average.desc&without_genres=99,10755&vote_count.gte=20&api_key=${tmdbApi}`
// const tmdbURL = `https://api.themoviedb.org/3/movie?api_key=${tmdbApi}&language=ko-KR`
// const tmdbURL = 'https://api.themoviedb.org/3/movies/get-top-rated-movies'

const movieList = ref()



axios.get(tmdbURL)
    .then((response) => {
        // console.log(response.data.results)
        movieList.value = response.data.results
    }).catch((error) => {
        console.log(error)
    })


const goToDetail = (movie) => {
    router.push(`/${movie.id}`)
}

</script>

<style scoped>


</style>

<style>
.movie-card img{
    width: 200px;
    height: 200px;
}
</style>