import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()

  const movieList = ref([
    {
      "model": "movies.movie",
      "pk": 872585,
      "fields": {
        "title": "오펜하이머",
        "original_title": "Oppenheimer",
        "overview": "세상을 구하기 위해 세상을 파괴할 지도 모르는 선택을 해야 하는 천재 과학자의 핵개발 프로젝트.",
        "release_date": "2023-07-19",
        "popularity": 2601.168,
        "vote_average": 8.2,
        "poster_path": "/4ZLnVUfiCe3wX8Ut9eyujndpyvA.jpg",
        "backdrop_path": "/rLb2cwF3Pazuxaj0sRXQ037tGI1.jpg"
      }
    },
    {
      "model": "movies.movie",
      "pk": 507089,
      "fields": {
        "title": "프레디의 피자가게",
        "original_title": "Five Nights at Freddy's",
        "overview": "80년대에 아이들이 실종되고 폐업한지 오래된 프레디의 피자가게 그곳의 야간 경비 알바를 하게 된 ‘마이크'는 캄캄한 어둠만이 존재하는 줄 알았던 피자가게에서 살아 움직이는 피자가게 마스코트 '프레디와 친구들’을 목격한다. 어딘가 기괴하고 섬뜩한 프레디와 친구들이 실체를 드러내기 시작하는데...",
        "release_date": "2023-10-25",
        "popularity": 1436.818,
        "vote_average": 8.0,
        "poster_path": "/h3hhfWdBhdb2JLMZprQ1IvBe90h.jpg",
        "backdrop_path": "/t5zCBSB5xMDKcDqe91qahCOUYVV.jpg"
      }
    },
    {
      "model": "movies.movie",
      "pk": 575264,
      "fields": {
        "title": "미션 임파서블: 데드 레코닝 PART ONE",
        "original_title": "Mission: Impossible - Dead Reckoning Part One",
        "overview": "모든 인류를 위협할 새로운 무기를 추적하게 된 에단 헌트와 IMF팀은 이 무기가 인류의 미래를 통제할 수 있다는 사실을 알게 된다. 전 세계가 위태로운 상황에 처한 가운데, 이를 추적하던 에단 헌트에게 어둠의 세력까지 접근하고 마침내 미스터리하고 강력한 빌런과 마주하게 된 그는 가장 위험한 작전을 앞두고 자신이 아끼는 사람들의 생명과 중요한 임무 사이에서 선택을 해야 하는 상황에 놓이게 되는데…",
        "release_date": "2023-07-08",
        "popularity": 1269.614,
        "vote_average": 7.6,
        "poster_path": "/nQsWPG020kSWdOl3EhFXRNE2s0n.jpg",
        "backdrop_path": "/628Dep6AxEtDxjZoGP78TsOxYbK.jpg"
      }
    },
    {
      "model": "movies.movie",
      "pk": 299054,
      "fields": {
        "title": "익스펜더블 4",
        "original_title": "Expend4bles",
        "overview": "테러 단체에게 핵미사일이 탈취되어 3차 세계대전이 발발할 위기의 상황에 ‘리’(제이슨 스타뎀)를 새로운 리더로 맞은 무적의 팀 익스펜더블이 작전에 투입되는데...",
        "release_date": "2023-09-15",
        "popularity": 1207.257,
        "vote_average": 6.482,
        "poster_path": "/dWR8OTRCcYDbBmd8GKsyJT73kU2.jpg",
        "backdrop_path": "/wl4NWiZwpzZH67HiDgpDImLyds9.jpg"
      }
    },
    {
      "model": "movies.movie",
      "pk": 385687,
      "fields": {
        "title": "분노의 질주: 라이드 오어 다이",
        "original_title": "Fast X",
        "overview": "돔과 그의 패밀리 앞에 나타난 운명의 적 단테. 과거의 그림자는 돔의 모든 것을 파괴하기 위해 달려온다. 단테에 의해 산산히 흩어진 패밀리들은 모두 목숨을 걸고 맞서야 하는 함정에 빠지고 마는데...",
        "release_date": "2023-05-17",
        "popularity": 820.632,
        "vote_average": 7.222,
        "poster_path": "/wXNihLltMCGR7XepN39syIlCt5X.jpg",
        "backdrop_path": "/4XM8DUTQb3lhLemJC51Jx4a2EuA.jpg"
      }
    },
    {
      "model": "movies.movie",
      "pk": 678512,
      "fields": {
        "title": "사운드 오브 프리덤",
        "original_title": "Sound of Freedom",
        "overview": "",
        "release_date": "2023-07-03",
        "popularity": 783.527,
        "vote_average": 8.088,
        "poster_path": "/qA5kPYZA7FkVvqcEfJRoOy4kpHg.jpg",
        "backdrop_path": "/pA3vdhadJPxF5GA1uo8OPTiNQDT.jpg"
      }
    },
  ])

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

  

  return { signup, logIn, token, movies, API_URL, router, movieList }
})
