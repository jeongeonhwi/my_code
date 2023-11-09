<template>
  <div>
    <header>
      <h1>명함 관리 페이지</h1>
    </header>
    <br>
    <br>
    <main>
      명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.
    </main>
    <article>
      <CreateCardForm @create-card-event="updateCard" />
      <businessCard :my-card="cardData"/>
    </article>
    <footer>
      2023 My Business Cards
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import businessCard from '@/components/businessCard.vue';
import CreateCardForm from '@/components/CreateCardForm.vue';
const cardData = ref('')

const updateCard = function(cardInfo) {
  cardData.value = cardInfo
  // console.log(typeof cardData)
}

</script>

<style scoped>
header {
  color: white;
  background-color: rgb(71, 71, 201);
  width: 35%;
  height: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}

div {
  text-align: center;
}

footer {
  height: 50px;
  background-color: rgb(236, 233, 233);
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>