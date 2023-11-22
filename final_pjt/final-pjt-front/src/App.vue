<template>
  <div>
    <div class="nav-bar">
    <nav>
      <div class="left-nav">
          <!-- Home, 추천 영화, 인기 배우 -->
          <!-- <RouterLink :to="{ name: 'main' }">Home</RouterLink> /
          <RouterLink :to="{ name: 'RecommendMovieView' }">추천 영화</RouterLink> / 
          <RouterLink :to="{ name: 'popularActors' }">인기배우</RouterLink> -->

          <router-link :to="{ name: 'main' }" class="btn btn-secondary">Home</router-link>
          <router-link :to="{ name: 'RecommendMovieView' }" class="btn btn-secondary">추천영화</router-link>
          <router-link :to="{ name: 'popularActors' }" class="btn btn-secondary">인기배우</router-link>
      </div>

      <!--검색기능-->
      <div>
        <input type="text" placeholder="영화 제목을 입력하세요." 
        :value="inputData" 
        @input="onInput">
        <button
        @click="findMovie"
        class="btn btn-secondary"
        >검색</button>
      </div>

      <div class="right-nav" v-if="!store.isLogin">
        <!-- 회원가입/로그인
        <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink> /
        <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink> -->
        <router-link :to="{ name: 'SignUpView' }" class="btn btn-secondary">회원가입</router-link>
        <router-link :to="{ name: 'LogInView' }" class="btn btn-secondary">로그인</router-link>

      </div>
      <div class="right-nav" v-if="store.isLogin">
        <!-- 로그아웃/마이페이지 -->
        <span @click="store.logOut" class="btn btn-secondary">로그아웃</span> 
        <!-- <RouterLink :to="{ name: 'mypage', params : {id: store.userId} }">마이페이지</RouterLink> -->
        <router-link :to="{ name: 'mypage', params : {id: store.userId} }" class="btn btn-secondary">로그인</router-link>
      </div>
    </nav>
    </div>
  </div>
  <!-- <h2 v-if="store.isLogin">{{ store.showUsername }}님 환영합니다</h2> -->
  <RouterView />
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterView, RouterLink, useRouter } from 'vue-router'
import { ref, reactive } from 'vue'
import axios from 'axios'

const store = useCounterStore()
const inputData = ref('')
const youtubeAPI = 'AIzaSyC3aKDsjdqG_4MLn4H4TJM0GtWWMXatAwc'
const router = useRouter()
const youtubeList = reactive([]);
const onInput = function (event) {
    inputData.value = event.currentTarget.value
}

const findMovie = function () {
  const searchWord = inputData.value;
  const youtubeURL = `https://www.googleapis.com/youtube/v3/search?key=${youtubeAPI}&part=snippet&type=video&q=${searchWord}`;
  axios.get(youtubeURL)
    .then((response) => {
      youtubeList.length = 0;
      youtubeList.push(...response.data.items);

      // Set search results in the store
      store.setSearchResults(youtubeList);

      

      if (youtubeList.length > 0) {
        router.push({ name: 'SearchResults' });
      }
    })
    .catch((error) => {
      console.log(error);
    });
}
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border: 1px solid black
  
}

.left-nav {
  display: flex;
  gap: 10px;
  color: white;
}

.right-nav {
  display: flex;
  gap: 10px;
}

.welcome-message {
  margin-top: 10px;
}

.nav-bar {
  background-color: black;
}
</style>