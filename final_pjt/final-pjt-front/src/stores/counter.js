import { ref, computed, watch, reactive } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const showUsername = ref(null)
  const userList = ref([])
  const userId = ref(null)
  const loginUser = ref(null)
  const router = useRouter()
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  //회원가입
  const signup = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
    .then((response) => {
      console.log('회원가입이 완료되었습니다.')
      router.push({ name: "main" })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  //로그인
  const logIn = function (payload) {
    const username = payload.username
    const password = payload.password

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        token.value = response.data.key
        showUsername.value = username
        console.log('로그인성공')
        console.log(showUsername)
        router.push({ name: "main"})
      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 로그아웃
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        localStorage.removeItem('token')
        // delete axios.defaults.headers.common['Authorization']
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  watch(showUsername, (newValue, oldValue) => {
    console.log('워치~~~~~~~~~')
    axios({
      method: 'get',
      url: `${API_URL}/accounts/${showUsername.value}/check_user_id/`,
    })
      .then((res) => {
        console.log(res.data.id)
        userId.value = res.data.id
        loginUser.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  })

   // 검색기능용
   const state = reactive({
    // ... (existing state properties)
    searchResults: reactive([]),
  });

  const setSearchResults = (results) => {
    state.searchResults = results;
  }
  

  return { state, userList, setSearchResults, signup, logIn, isLogin, logOut, token, movies, API_URL, router, loginUser, showUsername, userId }
}, { persist: true })