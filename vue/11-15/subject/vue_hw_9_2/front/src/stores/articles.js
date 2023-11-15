import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const token = ref(null)
  const router = useRouter()

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getArticles = function () {
    // console.log(token.value)
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => articles.value = res.data)
    .catch(err => {
      console.log(err)
    })
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      }
    })
    .then(res => console.log(res))
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url:'http://127.0.0.1:8000/accounts/signup/',
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log('회원가입이 완료되었습니다.')
        const payload1 = {
          username,
          password:password1
        }
        console.log(payload1)
        logIn(payload1)
      })
      .catch((error) => {
        console.log(error)
      })
  }
  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url:'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인이 완료되었습니다.')
        token.value = res.data.key
        router.push({name:'home'})
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return { articles, getArticles, createArticle, signUp, logIn, token, isLogin }
})
