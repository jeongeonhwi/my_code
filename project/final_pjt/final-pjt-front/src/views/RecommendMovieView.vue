<template>
  <div>
      <h1>추천 영화</h1>

      <h2>인기 있는 영화</h2>
      <div class="mainbox d-flex flex-wrap m-4">
        <div v-for="movie in recommendedMovies" :key="movie.pk"
        @click="goToDetail(movie.id)"
        >
          <img :src="getPosterUrl(movie)" alt="poster_path" class="img1 m-2">
        </div>
      </div>

      <h2>인기 있는 배우를 보고 싶다면?</h2>
      <div class="mainbox d-flex flex-wrap m-4">
        <div v-for="movie in actorPopulationMovies.related_movies" :key="movie.title"
        @click="goToDetail(movie.id)"
        >
          <img :src="getPosterUrl(movie)" alt="poster_path" class="img2 m-2">
        </div>
      </div>

      <h2>유명한 감독</h2>
      <div class="mainbox d-flex flex-wrap m-4">
        <div v-for="movie in directorPopulationMovies.related_movies" :key="movie.pk"
        @click="goToDetail(movie.id)"
        >
          <img :src="getPosterUrl(movie)" alt="poster_path" class="img3 m-2">
        </div>
      </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'


const router = useRouter()
const store = useCounterStore()
const recommendedMovies = ref([])
const actorPopulationMovies = ref([])
const directorPopulationMovies = ref([])

// 영화 인기도순
onMounted(async () => {
const apiUrl = 'http://127.0.0.1:8000/api/v1/recommended/';

try {
  const response = await axios.get(apiUrl);
  recommendedMovies.value = response.data;
} catch (error) {
  console.error('Django 데이터 가져오기 오류:', error);
}
});


// 배우 인기도 평균순
onMounted(async () => {
const apiUrl = 'http://127.0.0.1:8000/api/v1/actor_population_movies/';

try {
  const response = await axios.get(apiUrl);
  actorPopulationMovies.value = response.data;
  console.log(response.data)
  console.log(response.data.related_movies[0].poster)
} catch (error) {
  console.error('Django 데이터 가져오기 오류:', error);
}
});

// 감독 인기도 평균순
onMounted(async () => {
const apiUrl = 'http://127.0.0.1:8000/api/v1/director_population_movies/';

try {
  const response = await axios.get(apiUrl);
  directorPopulationMovies.value = response.data;
} catch (error) {
  console.error('Django 데이터 가져오기 오류:', error);
}
});

const getPosterUrl = (movie) => {
return `https://image.tmdb.org/t/p/w200${movie.poster_path}`;
};

const goToDetail = function(movieId) {
  router.push({name:'movieDetail', params: {movie_pk:movieId}})
}

</script>

<style scoped>

.mainbox {
display: flex;
}

h1 {
  
  text-align: center;
  margin-top: 100px;
  margin-bottom: 100px;
}

h2 {
  margin-top: 100px;
  margin-left: 20px;
}
.img1:hover {

  -webkit-transform: scale(1);
	transform: scale(1);
	-webkit-transition: .5s ease-in-out;
	transition: .5s ease-in-out;
  -webkit-transform: scale(1.3);
	transform: scale(1.3);
}


.img2:hover {
  -webkit-transform: scale(1);
	transform: scale(1);
	-webkit-transition: .5s ease-in-out;
	transition: .5s ease-in-out;
  -webkit-transform: scale(1.3);
	transform: scale(1.3);

}

.img3:hover {
  -webkit-transform: scale(1);
	transform: scale(1);
	-webkit-transition: .5s ease-in-out;
	transition: .5s ease-in-out;
  -webkit-transform: scale(1.3);
	transform: scale(1.3);

}

</style>