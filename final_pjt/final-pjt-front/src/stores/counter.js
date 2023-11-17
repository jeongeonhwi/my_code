import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()


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
        console.log('로그인성공')
        router.push({ name: "main"})
      })
      .catch((error) => {
        console.log(error)
      })
  }

  return { signup, logIn, token, movies, API_URL, router }
})
