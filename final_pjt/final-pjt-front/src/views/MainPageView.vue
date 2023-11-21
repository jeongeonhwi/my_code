<template>
    <!-- <div >
        <h1>최신개봉영화</h1>
            <MovieDetail
            v-for="movie in movies"
            :key="movie.id"
            :main-to-detail="movie"
            />
        
    </div> -->



  <div>
    <h1>최신개봉영화</h1>
    <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
      <div class="carousel-inner">
        <div v-for="(movie, index) in movies" :key="index" :class="{ 'carousel-item': true, 'active': index === 0 }"
        @click="goToDetail(movie.id)"
        >
          <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="d-block w-100 img-fluid" style="max-height: 400px; max-width:400px" alt="Movie Poster">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <div class="d-flex">
      <MovieDetail
      v-for="movie in movies"
      :key="movie.id"
      :main-to-detail="movie"
      />
    </div>
  </div>





</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import MovieDetail from '@/components/MovieDetail.vue'
import axios from 'axios';


const router = useRouter()
const store = useCounterStore()
const movies = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/latest/`
    })
        .then((res) => {
            movies.value = res.data
            // console.log(movies.value)
        })
        .catch((err) => {
            console.log(err)
        })
})

const goToDetail = function(movieId) {
  router.push({name:'movieDetail', params: {movie_pk:movieId}})
}
</script>

<style scoped>

</style>