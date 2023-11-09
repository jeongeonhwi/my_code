<template>
  <header>
<div class="modal modal-sheet position-static d-block bg-body-secondary p-4 py-md-5" tabindex="-1" role="dialog" id="modalTour">
  <div class="modal-dialog" role="document">
    <div class="modal-content rounded-4 shadow">
      <div class="modal-body p-5">
        <h2 class="fw-bold mb-0 text-center ">Quiz 퀴즈</h2>
        <ul class="d-grid gap-4 my-5 list-unstyled small">
          <li class="d-flex gap-4">
            <div>
              여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!
            </div>
          </li>
        </ul>
        <div class="container">
          <div class="row">
            <RouterLink :to="{name:'home'}" type="button" class="col-6 btn btn-lg btn-primary w-50 m-1" data-bs-dismiss="modal">HOME</RouterLink>
            <button type="button" class="col btn btn-lg btn-primary w-50 m-1" data-bs-dismiss="modal">퀴즈 목록</button>
            <button type="button" class="col-6 btn btn-lg btn-primary w-50 m-1" data-bs-dismiss="modal">퀴즈 생성</button>
            <button type="button" class="col btn btn-lg btn-primary w-50 m-1" data-bs-dismiss="modal">정답 확인</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</header>
<main>
  <RouterView />
</main>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
</script>

<style scoped>

</style>