<template>
    <div>
        <h1>무비 상세페이지</h1>
        <!-- <img :src="`https://image.tmdb.org/t/p/w200${props.mainToDetail.fields.poster_path}`" alt="poster_path">
        <p>{{ movie }}</p> -->
        <div>
            <RouterLink :to="`/detail/${ route.params.movie_pk }`">overview</RouterLink> /
            <RouterLink :to="`/detail/${ route.params.movie_pk }/cast`">cast</RouterLink> /
        </div>
        <router-view></router-view>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const movie = ref(null)

// onMounted(() => {
//     axios({
//         method: 'get',
//         url: `${store.API_URL}/api/v1/movies/${route.params.movie_pk}/`
//     })
//         .then((res) => {
//             // console.log(res.data)
//             movie.value = res.data
//         })
//         .catch((err) => {
//             console.log(err)
//         })
// })
</script>

<style scoped>

</style>