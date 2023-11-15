import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import { useArticleStore } from '@/stores/articles'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      beforeEnter: ((to, from) => {
        const store = useArticleStore()
        if (store.isLogin) {
          console.log('이미 로그인 되어 있습니다.')
          return { name: 'home'}
        }
      })
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView,
      beforeEnter: ((to, from) => {
        const store = useArticleStore()
        if (store.isLogin) {
          console.log('이미 로그인 되어 있습니다.')
          return { name: 'home'}
        }
      })
    },

  ]
})

export default router
