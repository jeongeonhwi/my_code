<template>
    <h3>보유 명함 목록</h3>
    <p v-if="countCard">현재 보유중인 명함 수 : {{ countCard }}</p>
    <p v-else>명함이 없습니다. 새로운 명함을 추가해 주세요.</p>
    <div class="box">
        <div v-for="BusinessCard in BusinessCards">
            <businessCardDetail 
            :my-msg="BusinessCard" 
            @delete="deleteCardFunc(BusinessCard)"
            />
        </div>
    </div>
</template>

<script setup>
import { ref, computed, watch, onDeactivated } from 'vue'
import businessCardDetail from '@/components/businessCardDetail.vue'

const BusinessCards = ref([
    {name:'일론 머스크', title:'테슬라 테크노킹'},
    {name:'래리 엘리슨', title:'오라클 창업주'},
    {name:'빌 게이츠', title:'마이크로소프트 공동창업주'},
    {name:'래리 페이지', title:'구글 공동창업주'},
    {name:'세르게이 브린', title:'구글 공동창업주'},
])

const deleteCardFunc = function(item) {
    const tmp_list = BusinessCards.value.filter((element) => element.name !== item.name);
    BusinessCards.value = tmp_list
}

const countCard = computed (() => {
    return BusinessCards.value.length
})

const props = defineProps({
    myCard:Object
})

// watch(() => props.myCard, (old, new) => {
//     console.log(old, new)
// })
watch(() => props.myCard, (next) => {
    BusinessCards.value.push(next)
    console.log(BusinessCards)
})

</script>

<style scoped>
.box {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
</style>