<template>
  <div>
      <h1>추천 영화</h1>
      <div class="mainbox">
        <li v-for="movie in recommendedMovies" :key="movie.pk">{{ movie.title }}
        <img :src="getPosterUrl(movie)" alt="poster_path">
        </li>
      </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const recommendedMovies = ref([]);


onMounted(async () => {
// Django 백엔드의 API 엔드포인트 URL을 설정합니다.
const apiUrl = 'http://127.0.0.1:8000/api/v1/recommended/';

try {
  // Axios를 사용하여 데이터를 가져옵니다.
  const response = await axios.get(apiUrl);
  // 성공적으로 데이터를 가져왔을 때 처리
  recommendedMovies.value = response.data;
  // console.log(response.data[0].poster_path)
} catch (error) {
  // 오류가 발생했을 때 처리
  console.error('Django 데이터 가져오기 오류:', error);
}
});
const getPosterUrl = (movie) => {
return `https://image.tmdb.org/t/p/w200${movie.poster_path}`;
};



</script>

<style scoped>
.mainbox {
display: flex;  
}

</style>