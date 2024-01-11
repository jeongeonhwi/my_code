import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import RecommendMovieView from '@/views/RecommendMovieView.vue'
import overview from '@/components/overview.vue'
import cast from '@/components/cast.vue'
import PopularActorView from '@/views/PopularActorView.vue'
import MyPageView from '@/views/MyPageView.vue'
import SearchResultsView from '@/views/SearchResultsView.vue'
import ThreeDPage from '@/views/ThreeDPage.vue'
import { useCounterStore } from '@/stores/counter'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ThreeDPage',
      component: ThreeDPage,
    },
    {
      path: '/main',
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
    {
      path: '/mypage/:id',
      name: 'mypage',
      component: MyPageView,
      meta: {
        requiresAuth: true // 로그인 상태를 확인하기 위한 메타 필드 추가
      },
      // beforeEnter: (to, from) => {
      //   const store = useCounterStore()
      //   console.log(to.params.id)
      //   console.log(store.userId)
      //   console.log(store.userList)
      //   if ((store.userId != to.params.id)&&(store.userList.some(obj => obj.id == to.params.id))) {
      //     router.push({name:'main'})
      //   } else {
      //     console.log(store.userList.some(obj => obj.id === to.params.id))
      //   }
      // }
    },
    {
      path: '/search-results',
      name: 'SearchResults',
      component: SearchResultsView
    }
  ]
})

export default router
