<template>
  <div>
    <MovieSwiper 
    :main-to-swiper="movies"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import MovieDetail from '@/components/MovieDetail.vue'
import axios from 'axios';
import MovieSwiper from '@/components/MovieSwiper.vue'


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
.mainview {
  text-align: center;
}

#carouselExampleAutoplaying{
  align-items: center;
}

</style>