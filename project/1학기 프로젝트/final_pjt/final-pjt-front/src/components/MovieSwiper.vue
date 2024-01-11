<template>
  <div class="swiper mySwiper" @wheel="handleMouseWheel">
    <h1>최신 개봉 영화</h1>
    <br>
    <br>
    <div class="swiper-wrapper">
      <div v-for="movie in mainToSwiper" class="swiper-slide" :key="movie.id" @click="goToDetail(movie.id)" @mouseover="handleMouseOver" @mouseout="handleMouseOut">
        <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="slide-image">
      </div>
    </div>
    <div class="swiper-pagination"></div>
  </div>
</template>

<script setup>
import 'swiper/css';
import Swiper from 'swiper/bundle';
import { onMounted, defineProps } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const props = defineProps({
  mainToSwiper: Array,
});

let swiper;

onMounted(() => {
  swiper = new Swiper(".mySwiper", {
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
  router.push({ name: 'movieDetail', params: { movie_pk: movieId } });
};

const handleMouseOver = (event) => {
  const swiperSlide = swiper.slides[swiper.activeIndex];
  if (event.currentTarget === swiperSlide) {
    const image = event.currentTarget.querySelector('.slide-image');
    image.style.transition = "transform 0.5s ease-in-out";
    image.style.transform = "scale(1.1)";
  }
};

const handleMouseOut = (event) => {
  const swiperSlide = swiper.slides[swiper.activeIndex];
  if (event.currentTarget === swiperSlide) {
    const image = event.currentTarget.querySelector('.slide-image');
    image.style.transition = "transform 0.5s ease-in-out";
    image.style.transform = "scale(1)";
  }
};

const handleMouseWheel = (event) => {
  if (event.deltaY > 0) {
    swiper.slideNext();
  } else {
    swiper.slidePrev();
  }
};
</script>

<style scoped>
/* Your component styles go here */
.swiper-slide {
  width: 250px;
  transition: transform 0.5s ease-in-out;
}

.slide-image {
  display: block;
  width: 400px;
  -webkit-box-reflect: below 1px linear-gradient(transparent, transparent, #0002, #0004);
}

h1 {
  text-align: center;
  margin-top: 100px;
}
</style>
