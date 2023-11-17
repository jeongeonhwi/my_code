import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPageView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
      
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})

export default router
