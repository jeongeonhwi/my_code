<template>
    <div>
        <br>
        <br>
        <form @click.prevent="">
        <label for="name"> 이름 </label>
        <input type="text" id="name" v-model="cardName">
        <label for="career"> 직함 </label>
        <input type="text" id="career" v-model="cardCareer">
        <button 
        @click="createCardFunc" 
        >명함 추가</button>
        </form>
        <br>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const cardName = ref('')
const cardCareer = ref('')
const emit = defineEmits(['createCardEvent'])

const createCardFunc = function () {
    const cardInfo = {name:cardName.value, title:cardCareer.value}
    // console.log(cardInfo)
    emit('createCardEvent', cardInfo)
    cardName.value = ''
    cardCareer.value = ''
}
</script>

<style scoped>

</style>