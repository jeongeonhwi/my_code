import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import PostlistView from '@/views/PostlistView.vue'
import CategoryCreateView from '@/views/CategoryCreateView.vue'
import PostCreateView from '@/views/PostCreateView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: MainView
    },
    {
      path: '/post',
      name: 'postList',
      component: PostlistView
    },
    {
      path: '/category',
      name: 'category',
      component: CategoryCreateView
    },
    {
      path: '/postcreate',
      name: 'postcreate',
      component: PostCreateView
    },
  ]
})

export default router
