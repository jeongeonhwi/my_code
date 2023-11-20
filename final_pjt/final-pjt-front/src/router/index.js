import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import RecommendMovieView from '@/views/RecommendMovieView.vue'
import overview from '@/components/overview.vue'
import cast from '@/components/cast.vue'
import PopularActorView from '@/views/PopularActorView.vue'


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
    },
    {
      path: '/detail/:movie_pk',
      name: 'movieDetail',
      component: MovieDetailView,
    },
    {
      path: '/recommend',
      name: 'RecommendMovieView',
      component: RecommendMovieView
    },
    {
      path: '/popularActors',
      name: 'popularActors',
      component: PopularActorView
    },
  ]
})

export default router
