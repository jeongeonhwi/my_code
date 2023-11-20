<template>
    <div v-if="movie">
        <h1>무비 상세페이지</h1>
        <img :src="`https://image.tmdb.org/t/p/w200${movie.poster_path}`" alt="poster_path">
        <p>
            <span @click="overviewClick">overview</span> | 
            <span @click="castClick">cast</span> | 
            <span @click="reviewClick">review</span> | 
            <span @click="previewClick">preview</span>
        </p>
        <div v-show="overviewShow">
            <h4>overview</h4>
            <p>{{ movie.title }}</p>
            <p>{{ movie.overview }}</p>
        </div>
        <div v-show="castShow" v-if="actors">
            <h4>cast</h4>
            <div v-for="director in directors"
            :key="director.id">
                <p>director</p>
                <img :src="`https://image.tmdb.org/t/p/w200${director.profile_path}`" alt="profile_path">
                {{ director.name }}
            </div>

            <p>actor</p>
            <!-- {{ actors }} -->
            <div v-for="actor in actors"
            :key="actor.id">
                <img :src="`https://image.tmdb.org/t/p/w200${actor.profile_path}`" alt="profile_path">
                {{ actor.name }}
            </div>
        </div>
        <div v-show="reviewShow">
            <h4>review</h4>
            <ReviewDetail
            v-for="review in reviews"
            :key="review.id"
            :movie-to-review="review"
            />
            <form @submit.prevent="createReview">
              <p>별점과 리뷰를 작성해주세요.</p>
              <select v-model="score">
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
              <input type="text" v-model="content">
              <input type="submit">
            </form>
        </div>
        <div v-show="previewShow">
            <h4>preview</h4>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
import ReviewDetail from '@/components/ReviewDetail.vue'

const overviewShow = ref(true)
const castShow = ref(false)
const reviewShow = ref(false)
const previewShow = ref(false)
const store = useCounterStore()
const route = useRoute()
const movie = ref(null)
const actors = ref(null)
const directors = ref(null)
const score = ref(null)
const content = ref(null)
const reviews = ref(null)


onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/movies/${route.params.movie_pk}/`
    })
        .then((res) => {
            // console.log(res.data)
            movie.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
})

const overviewClick = function () {
    overviewShow.value = true
    castShow.value = false
    reviewShow.value = false
    previewShow.value = false
}

const castClick = function () {
    overviewShow.value = false
    castShow.value = true
    reviewShow.value = false
    previewShow.value = false

    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/movies/${route.params.movie_pk}/actor/`
    })
        .then((res) => {
            // console.log(res.data)
            actors.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
    
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/movies/${route.params.movie_pk}/director/`
    })
        .then((res) => {
            // console.log(res.data)
            directors.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
}

const reviewClick = function () {
    overviewShow.value = false
    castShow.value = false
    reviewShow.value = true
    previewShow.value = false
}

const previewClick = function () {
    overviewShow.value = false
    castShow.value = false
    reviewShow.value = false
    previewShow.value = true
}

const redirectReview = function () {
  axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/review/${route.params.movie_pk}/`,
      headers: {
        Authorization: `Token ${store.token}`
    },
    })
        .then((res) => {
            // console.log(res.data)
            reviews.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
}

const createReview = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/review/${route.params.movie_pk}/`,
    data: {
      score: score.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    },
  }).then(() => {
    console.log('리뷰작성이 완료되었습니다.')
    content.value = null
    score.value = null
    redirectReview()
  }).catch(err => {
    console.log('오류오류!!!!')
    console.log(store.token)
    console.log(err)
  })
}

onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/review/${route.params.movie_pk}/`,
      headers: {
        Authorization: `Token ${store.token}`
    },
    })
        .then((res) => {
            // console.log(res.data)
            reviews.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
})
</script>

<style scoped>

</style>