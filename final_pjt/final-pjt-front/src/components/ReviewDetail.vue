<template>
    <div>
        <h4>리뷰컴포넌트</h4>
        <span v-show="putToggle">
            <span @click="goToMyPage(props.movieToReview.user)">
                유저 : {{ props.movieToReview.user }} | 
            </span>
            별점 : {{ props.movieToReview.score }} | {{ props.movieToReview.content }}
        </span>
        <form @submit.prevent="reviewPut" v-show="!putToggle">
            <select v-model="score">
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            <input type="text" 
            v-model="content"
            >
            <input type="submit">
        </form>
        <button @click="reviewDelete">삭제</button>
        <button @click="togglePut" v-show="putToggle">수정</button>
        <button @click="togglePut" v-show="!putToggle">수정취소</button>
    </div>
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

</style>