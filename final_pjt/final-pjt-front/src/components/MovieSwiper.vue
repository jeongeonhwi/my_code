<template>
    <div class="swiper mySwiper">
      <h1>최신 영화</h1>
      <br>
      <br>
      <div class="swiper-wrapper">
        <div v-for="movie in mainToSwiper" class="swiper-slide" :key="movie.id" @click="goToDetail(movie.id)">
          <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`">
        </div>
      </div>
      <div class="swiper-pagination"></div>
    </div>
  </template>
  
  <script setup>
  import 'swiper/css';
  import Swiper from 'swiper/bundle';
  import { onMounted, defineProps } from 'vue';
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  const props = defineProps({
    mainToSwiper: Array
  })
  
  onMounted(() => {
    const swiper = new Swiper(".mySwiper", {
      effect: "coverflow",
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: "auto",
      coverflowEffect: {
        rotate: 10,
        stretch: 0,
        depth: 500,
        modifier: 1,
        slideShadows: true,
      },
      loop: true,
    });
  });
  
  const goToDetail = function(movieId) {
    router.push({name:'movieDetail', params: {movie_pk:movieId}})
  }
  </script>
  
  <style scoped>
  /* Your component styles go here */
  img {
    width: 800px;
    height: auto;
  }
  .swiper {
    width: 80%;
    padding-top: 50px;
  }
  
  .swiper-slide {
    background-position: center;
    background-size: cover;
    width: 250px;
  }
  
  .swiper-slide img {
    display: block;
    width: 400px;
    -webkit-box-reflect: below 1px linear-gradient(transparent, transparent, #0002, #0004);
  }
  
  h1 {
    text-align: center;
  }
  </style>