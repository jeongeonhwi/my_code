<template>
  <div v-if="movie">
    <div class="background-container" :style="{ backgroundImage: `url('https://image.tmdb.org/t/p/w500${movie.backdrop_path}')` }">
    </div>
    <img class="opacity-img" :src="`https://image.tmdb.org/t/p/w200${movie.poster_path}`" alt="poster_path">
    <div>
            <ul class="nav nav-pills nav-fill gap-2 p-1 small bg-secondary rounded-5 shadow-sm" id="pillNav2" role="tablist" style="--bs-nav-link-color: var(--bs-white); --bs-nav-pills-link-active-color: var(--bs-secondary); --bs-nav-pills-link-active-bg: var(--bs-white);">
              <li class="nav-item" role="presentation">
                <button @click="overviewClick" class="nav-link active rounded-5" id="home-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="true">Overview</button>
              </li>
              <li class="nav-item" role="presentation">
                <button @click="castClick" class="nav-link rounded-5" id="profile-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="false">Cast</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button @click="reviewClick" class="nav-link rounded-5" id="contact-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="false">Review</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button @click="previewClick" class="nav-link rounded-5" id="contact-tab2" data-bs-toggle="tab" type="button" role="tab" aria-selected="false">Preview</button>
                </li>
              </ul>
            </div>
            
            <!-- {{ movie }} -->
        <div v-show="overviewShow" class="ms-4 mt-3">
            <!-- <h4>overview</h4> -->
            <h3>{{ movie.title }}</h3>
            <p>개봉 : {{ movie.release_date }}</p>
            <div class="d-flex">
              <div>
                별점 :&nbsp;
              </div>
              <div class="star-ratings">
                <div 
                  class="star-ratings-fill space-x-2 text-lg"
                  :style="{ width: `${star}%` }"
                > 
                <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                </div>
                <div class="star-ratings-base space-x-2 text-lg">
                  <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                </div>
              </div>
            </div>
            <br>
            <p>줄거리</p>
            <p>{{ movie.overview }}</p>
            
        </div>
        <div v-show="castShow" v-if="actors" class="ms-4">
            <!-- <h4>cast</h4> -->
            <br>
            <p class="ms-2 fs-3">감독</p>
            <div v-for="director in directors"
            :key="director.id">
                <div class="card m-2" style="width: 9rem;">
                    <img :src="`https://image.tmdb.org/t/p/w200${director.profile_path}`" class="card-img-top" alt="profile_path">
                    <div class="card-body">
                        <p class="card-text text-center">{{ director.name }}</p>
                    </div>
                </div>

            </div>
            <br>
            <p class="ms-2 fs-3">배우</p>
            <div class="d-flex flex-row mb-3">
                <div v-for="actor in actors"
                :key="actor.id"
                >
                    <div class="card m-2" style="width: 9rem;">
                        <img :src="`https://image.tmdb.org/t/p/w200${actor.profile_path}`" alt="profile_path">
                        <div class="card-body">
                            <p class="card-text text-center">{{ actor.name }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-show="reviewShow" class="ms-4">
            <!-- <h4>review</h4> -->
            <br>
            <ReviewDetail
            v-for="review in reviews"
            :key="review.id"
            :movie-to-review="review"
            :movie-to-review-movie="movie"
            />
            <br>
            <p>별점과 리뷰를 작성해주세요.</p>
            <form @submit.prevent="createReview" class="d-flex">
              <select v-model="score" class="form-select" style="width: 14%; height: 50%;">
                <option disabled selected>고르세요</option>
                <option value="0">&#10032;&#10032;&#10032;&#10032;&#10032;</option>
                <option value="1">★&#10032;&#10032;&#10032;&#10032;</option>
                <option value="2">★★&#10032;&#10032;&#10032;</option>
                <option value="3">★★★&#10032;&#10032;</option>
                <option value="4">★★★★&#10032;</option>
                <option value="5">★★★★★</option>
              </select>
              <input v-model="content" class="form-control" list="datalistOptions" id="exampleDataList" placeholder="리뷰를 입력하세요." style="width: 35%;">
              <button type="submit" class="btn btn-secondary">작성</button>



            </form>
        </div>
        <div v-show="previewShow">
            <!-- <h4>preview</h4> -->
            <br>
            <div v-if="youtubeList" class="ms-4">
                <!-- 첫 번째 예고편만을 출력합니다. -->
                <iframe :src="'https://www.youtube.com/embed/'+ youtubeList[0].id.videoId" width="560" height="315" frameborder="0" allowfullscreen></iframe>
                <p class="m-2">&nbsp;&nbsp;{{ youtubeList[0].snippet.title }}</p>
            </div>
        </div>
    </div>
    <br>
    <br>
    <br>
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
const score = ref('고르세요')
const content = ref(null)
const reviews = ref(null)
const star = ref(0)


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

const youtubeList = ref('')
const previewClick = function () {
    overviewShow.value = false
    castShow.value = false
    reviewShow.value = false
    previewShow.value = true
    

    const youtubeAPI = 'AIzaSyC3aKDsjdqG_4MLn4H4TJM0GtWWMXatAwc'
    const searchWord = `${movie.value.title} 예고편`
    const youtubeURL = `https://www.googleapis.com/youtube/v3/search?key=${youtubeAPI}&part=snippet&type=video&q=${searchWord}`
   
    // API를 통해 예고편 데이터를 가져옴
    axios.get(youtubeURL)
        .then((response) => {
            youtubeList.value = response.data.items
            // console.log(youtubeList.value[0].id.videoId)
        }).catch((error) => {
            console.log(error)
        })
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
            caculateStar()
        })
        .catch((err) => {
            console.log(err)
        })
})

const caculateStar = function() {
  console.log(reviews.value)
  if (reviews.value !== null) {
    const totalScore = reviews.value.reduce((acc, review) => acc + review.score, 0);
    const averageScore = totalScore / reviews.value.length;
    star.value = averageScore/5 * 100
  }
}
</script>

<style scoped>
.container {
  position: relative;
}
.background-container {
  width: 100%; /* div의 너비를 화면에 꽉 차게 설정 */
  height: 400px; /* div의 높이를 조절 */
  background-size: cover; /* 이미지가 화면에 꽉 차도록 설정 */
  background-position: center; /* 이미지를 가운데 정렬 */
  background-repeat: no-repeat; /* 이미지를 반복하지 않도록 설정 */
  /* background-color: rgba(0, 0, 0, 0); 배경 색에 불투명도 추가 (0.5는 50%의 불투명도를 나타냄) */
  opacity: 0.5;
  position: relative;
}

.opacity-img {
  margin-top: 20px;
  opacity: 1;
  position: absolute;
  top: 70px;
  left: 10px;
  /* z-index: 1; */
}

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

</style>