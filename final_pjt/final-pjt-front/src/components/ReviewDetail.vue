<template>
    <div>
        <!-- <h4>리뷰컴포넌트</h4> -->
        <span v-show="putToggle" class="ms-2">
            <span v-if="props.movieToReview.score === 0">&#10032;&#10032;&#10032;&#10032;&#10032; </span>
            <span v-if="props.movieToReview.score === 1">★&#10032;&#10032;&#10032;&#10032; </span>
            <span v-if="props.movieToReview.score === 2">★★&#10032;&#10032;&#10032; </span>
            <span v-if="props.movieToReview.score === 3">★★★&#10032;&#10032; </span>
            <span v-if="props.movieToReview.score === 4">★★★★&#10032; </span>
            <span v-if="props.movieToReview.score === 5">★★★★★ </span>
            <span class="fs-6">{{ props.movieToReview.score }}</span>
            <p class="m-1 ms-2">{{ props.movieToReview.content }}</p>
            <span @click="goToMyPage(props.movieToReview.user)" v-if="user" class="ms-2">
                {{ user.username.slice(0,4) }}****  
            </span>
            <span class="review-color">
                {{ props.movieToReview.updated_at.slice(0,10) }}. 
                {{ props.movieToReview.updated_at.slice(11, 16) }}&nbsp;
            </span>
        </span>
        <form @submit.prevent="reviewPut" v-show="!putToggle" >
            <div class="d-flex">
                <select v-model="score" class="form-select" style="width: 14%; height: 50%;">
                    <option disabled selected>고르세요</option>
                    <option value="0">&#10032;&#10032;&#10032;&#10032;&#10032;</option>
                    <option value="1">★&#10032;&#10032;&#10032;&#10032;</option>
                    <option value="2">★★&#10032;&#10032;&#10032;</option>
                    <option value="3">★★★&#10032;&#10032;</option>
                    <option value="4">★★★★&#10032;</option>
                    <option value="5">★★★★★</option>
                </select>


                <input type="text" v-model="content">
                <button type="submit" class="btn btn-secondary">수정</button>
            </div>
        </form>
        <span @click="togglePut" v-show="putToggle" v-if="props.movieToReview.user === store.userId" class="review-color">수정</span>
        <span v-show="putToggle"> &#8231; </span>
        <span @click="reviewDelete" v-if="props.movieToReview.user === store.userId" class="review-color">삭제</span>
        <span v-show="!putToggle"> &#8231; </span>
        <span @click="togglePut" v-show="!putToggle" v-if="props.movieToReview.user === store.userId" class="review-color">수정취소</span>
    </div>
    <hr>
</template>

<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { ref, computed, onMounted } from 'vue'


const score = ref(null)
const content = ref(null)
const putToggle = ref(true)
const router = useRouter()
const store = useCounterStore()
const props = defineProps({
    movieToReview:Object,
    movieToReviewMovie:Object,
})
const user = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/accounts/${props.movieToReview.user}/user/`
    })
        .then((res) => {
            // console.log(res.data)
            user.value = res.data
            // console.log(user.value)
        })
        .catch((err) => {
            console.log(err)
        })
})


const togglePut = function() {
    putToggle.value = !putToggle.value
    content.value = props.movieToReview.content
    score.value = props.movieToReview.score
}

const reviewDelete = function() {
    axios({
        method: 'delete',
        url: `${store.API_URL}/api/v1/review/${props.movieToReviewMovie.id}/${props.movieToReview.id}/`,
        headers: {
        Authorization: `Token ${store.token}`
    },
    })
        .then((res) => {
            console.log(`댓글 삭제가 완료되었습니다. ${res}`)
            location.reload();
        })
        .catch((err) => {
            console.log(err)
        })
}

const reviewPut = function() {
    axios({
        method: 'put',
        url: `${store.API_URL}/api/v1/review/${props.movieToReviewMovie.id}/${props.movieToReview.id}/`,
        data: {
            score: score.value,
            content: content.value
        },
        headers: {
        Authorization: `Token ${store.token}`
    },
    })
        .then((res) => {
            console.log(`댓글 수정이 완료되었습니다. ${res}`)
            location.reload();
        })
        .catch((err) => {
            console.log(err)
        })
}

const goToMyPage = function (userId) {
    router.push({name:'mypage', params: {id:userId}})
}
</script>

<style scoped>
.star-ratings {
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  color: aqua;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: aqua;
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
}

.review-color {
    color: #aaa9a9;
}
</style>