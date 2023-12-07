<template>
  <div>
      <h1>인기배우</h1>
      <div class="mainbox d-flex flex-wrap m-4">
        <div v-for="actor in popularActors" :key="actor.pk" class="d-flex flex-column">
          <img :src="getPosterUrl(actor)" alt="profile_path" class="img1 m-2">
          {{ actor.name }}
        </div>
      </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const popularActors = ref([]);


onMounted(async () => {
// Django 백엔드의 API 엔드포인트 URL을 설정합니다.
const apiUrl = 'http://127.0.0.1:8000/api/v1/popular_actor/';

try {
  // Axios를 사용하여 데이터를 가져옵니다.
  const response = await axios.get(apiUrl);
  // 성공적으로 데이터를 가져왔을 때 처리
  popularActors.value = response.data;
  // console.log(response.data[0].poster_path)
} catch (error) {
  // 오류가 발생했을 때 처리
  console.error('Django 데이터 가져오기 오류:', error);
}
});
const getPosterUrl = (actor) => {
return `https://image.tmdb.org/t/p/w200${actor.profile_path}`;
};



</script>

<style scoped>
.mainbox {
display: flex;  
}
.img1:hover {

-webkit-transform: scale(1);
transform: scale(1);
-webkit-transition: .5s ease-in-out;
transition: .5s ease-in-out;
-webkit-transform: scale(1.3);
transform: scale(1.3);
}

</style>