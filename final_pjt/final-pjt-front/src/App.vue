<template>
  <div>
    <div class="nav-bar">
    <nav>
      <div class="left-nav">
          <!-- Home, 추천 영화, 인기 배우 -->
          <div class="d-flex flex-column align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-house" viewBox="0 0 16 16">
              <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293zM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5z"/>
            </svg>
              <router-link :to="{ name: 'main' }" class="btn text-white">Home</router-link>
          </div>

          <div class="d-flex flex-column align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-hand-thumbs-up-fill" viewBox="0 0 16 16">
              <path d="M6.956 1.745C7.021.81 7.908.087 8.864.325l.261.066c.463.116.874.456 1.012.965.22.816.533 2.511.062 4.51a9.84 9.84 0 0 1 .443-.051c.713-.065 1.669-.072 2.516.21.518.173.994.681 1.2 1.273.184.532.16 1.162-.234 1.733.058.119.103.242.138.363.077.27.113.567.113.856 0 .289-.036.586-.113.856-.039.135-.09.273-.16.404.169.387.107.819-.003 1.148a3.163 3.163 0 0 1-.488.901c.054.152.076.312.076.465 0 .305-.089.625-.253.912C13.1 15.522 12.437 16 11.5 16H8c-.605 0-1.07-.081-1.466-.218a4.82 4.82 0 0 1-.97-.484l-.048-.03c-.504-.307-.999-.609-2.068-.722C2.682 14.464 2 13.846 2 13V9c0-.85.685-1.432 1.357-1.615.849-.232 1.574-.787 2.132-1.41.56-.627.914-1.28 1.039-1.639.199-.575.356-1.539.428-2.59z"/>
            </svg>
              <router-link :to="{ name: 'RecommendMovieView' }" class="btn text-white">추천영화</router-link>
          </div>
          
          <div class="d-flex flex-column align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-people" viewBox="0 0 16 16">
              <path d="M15 14s1 0 1-1-1-4-5-4-5 3-5 4 1 1 1 1zm-7.978-1A.261.261 0 0 1 7 12.996c.001-.264.167-1.03.76-1.72C8.312 10.629 9.282 10 11 10c1.717 0 2.687.63 3.24 1.276.593.69.758 1.457.76 1.72l-.008.002a.274.274 0 0 1-.014.002H7.022ZM11 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4m3-2a3 3 0 1 1-6 0 3 3 0 0 1 6 0M6.936 9.28a5.88 5.88 0 0 0-1.23-.247A7.35 7.35 0 0 0 5 9c-4 0-5 3-5 4 0 .667.333 1 1 1h4.216A2.238 2.238 0 0 1 5 13c0-1.01.377-2.042 1.09-2.904.243-.294.526-.569.846-.816M4.92 10A5.493 5.493 0 0 0 4 13H1c0-.26.164-1.03.76-1.724.545-.636 1.492-1.256 3.16-1.275ZM1.5 5.5a3 3 0 1 1 6 0 3 3 0 0 1-6 0m3-2a2 2 0 1 0 0 4 2 2 0 0 0 0-4"/>
            </svg>
            <router-link :to="{ name: 'popularActors' }" class="btn text-white">인기배우</router-link>
          </div>

          <div class="d-flex flex-column align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-chat-left-text-fill" viewBox="0 0 16 16">
              <path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H4.414a1 1 0 0 0-.707.293L.854 15.146A.5.5 0 0 1 0 14.793zm3.5 1a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1zm0 2.5a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1zm0 2.5a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1z"/>
            </svg>
            <a href="http://127.0.0.1:8000/chat/lobby/" class="btn text-white" style="text-decoration: none; color: white;">실시간채팅</a>
          </div>
      </div>

      <!--검색기능-->
      <form @submit.prevent="findMovie" class="d-flex">
        <input type="text" placeholder="영화 제목을 입력하세요." 
              :value="inputData" 
              class="inputbox"
              size="20"
              @input="onInput">
        <button type="submit" class="btn text-white">검색</button>
      </form>

      <div class="right-nav" v-if="!store.isLogin">
        <!-- 회원가입/로그인 -->
        <router-link :to="{ name: 'SignUpView' }" class="btn text-white">회원가입</router-link>
        <router-link :to="{ name: 'LogInView' }" class="btn text-white">로그인</router-link>

      </div>
      <div class="right-nav" v-if="store.isLogin">
        <!-- 로그아웃/마이페이지 -->
        <span @click="store.logOut" class="btn text-white">로그아웃</span> 
        <router-link :to="{ name: 'mypage', params : {id: store.userId} }" class="btn text-white">마이페이지</router-link>
       
      </div>
    </nav>
    </div>
  </div>
  <!-- <h2 v-if="store.isLogin">{{ store.showUsername }}님 환영합니다</h2> -->
  <transition name="fade-up" mode="out-in">
    <RouterView />
  </transition>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterView, RouterLink, useRouter } from 'vue-router'
import { ref, reactive, watch } from 'vue'
import axios from 'axios'

const store = useCounterStore()
const inputData = ref('')
const youtubeAPI = 'AIzaSyC3aKDsjdqG_4MLn4H4TJM0GtWWMXatAwc'
const router = useRouter()
const youtubeList = reactive([]);
// const currentRoute = ref(router.currentRoute.value.name);

// watch(() => {
//   currentRoute.value = router.currentRoute.value.name;
// }, { immediate: true });

const onInput = function (event) {
    inputData.value = event.currentTarget.value
}

const findMovie = function () {
  const searchWord = inputData.value;
  // const youtubeURL = `https://www.googleapis.com/youtube/v3/search?key=${youtubeAPI}&part=snippet&type=video&q=${searchWord}`;
  axios.get(`${store.API_URL}/api/v1/movies/${searchWord}`)
    .then((response) => {
      // youtubeList.length = 0;
      // youtubeList.push(...response.data.items);

      // // Set search results in the store
      // store.setSearchResults(youtubeList);

      

      // if (youtubeList.length > 0) {
      //   router.push({ name: 'SearchResults' });
      // }
        console.log(response.data[0].id)
        router.push({name:'movieDetail', params:{movie_pk:response.data[0].id}})
        
        setTimeout(() => {
          location.reload();
      }, 100);
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
  background-color: #800000;
  font-size: 1rem;
}

.inputbox {
  border-radius: 10px;
  text-align: center;
}
.fade-up-enter-active, .fade-up-leave-active {
  animation: fade-up-down 1.5s;
}

@keyframes fade-up-down {
  from {
    opacity: 0;
    transform: translateY(-100px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


</style>