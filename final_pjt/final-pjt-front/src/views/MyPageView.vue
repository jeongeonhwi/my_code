<template>
  <div  v-if="user">
    <h1>{{ user.username }}님의 페이지</h1>
    <p v-if="loginUser.id != user.id">
      <span v-if="!loginUser.like.includes(user.id)"
      @click="goToLike"
      >
        좋아요
      </span>
      <span v-if="loginUser.like.includes(user.id)"
      @click="goToLike"
      >
        좋아요 취소
      </span>
      | 
      <span v-if="!loginUser.hate.includes(user.id)"
      @click="goToHate"
      >
        싫어요
      </span>
      <span v-if="loginUser.hate.includes(user.id)"
      @click="goToHate"
      >
        싫어요 취소
      </span>
    </p>
    <!-- <p>{{ user }}</p> -->
    <h2>{{ user.username }}가 작성한 리뷰목록</h2>
    <MyPageReview
    v-for="review in reviews"
    :key="review.id"
    :mypage-to-review="review"
    />
    <h2>{{ user.username }}가 좋아요 누른 유저목록</h2>
    <likeUser
    v-for="like in user.like"
    :mypage-to-like="like"
    />
    <h2>{{ user.username }}가 싫어요 누른 유저목록</h2>
    <hateUser
    v-for="hate in user.hate"
    :mypage-to-hate="hate"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
import MyPageReview from '@/components/MyPageReview.vue/'
import likeUser from '@/components/likeUser.vue/'
import hateUser from '@/components/hateUser.vue/'


const router = useRouter()
const route = useRoute()
const store = useCounterStore()
const user = ref(null)
const reviews = ref(null)
const loginUser = ref(store.loginUser)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/accounts/${route.params.id}/user/`
    })
        .then((res) => {
            // console.log(res.data)
          user.value = res.data

          return axios({
            method: 'get',
            url: `${store.API_URL}/accounts/${route.params.id}/user_review/`
          })
            .then((res) => {
              reviews.value = res.data
              
            })
            .catch((err) => {
              
            })

        })
        .catch((err) => {
            console.log(err)
        })
})

const goToLike = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/accounts/${route.params.id}/user_like/`,
    headers: {
        Authorization: `Token ${store.token}`
    },
  })
    .then((res) => {
      console.log('좋아요 성공')
      const absolutePath = `/mypage/${loginUser.value.id}`
      router.push(absolutePath)

      // 일정 시간(예: 100ms)을 기다린 후에 리로드 실행 router.push는 비동기이기 때문
      setTimeout(() => {
          location.reload();
      }, 100);
    })
    .catch((err) => {
      console.log('좋아요 실패')
    })
}

const goToHate = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/accounts/${route.params.id}/user_hate/`,
    headers: {
        Authorization: `Token ${store.token}`
    },
  })
    .then((res) => {
      console.log('싫어요 성공')
      const absolutePath = `/mypage/${loginUser.value.id}`
      router.push(absolutePath)

      // 일정 시간(예: 100ms)을 기다린 후에 리로드 실행 router.push는 비동기이기 때문
      setTimeout(() => {
          location.reload();
      }, 100);
    })
    .catch((err) => {
      console.log('싫어요 실패')
    })
}


</script>

<style scoped>

</style>