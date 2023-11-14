import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res => {
      console.log(res.data)
      articles.value = res.data
    })
      .catch((error) => {
      console.log(error)
    })
  }

  return { articles, getArticles }
})
