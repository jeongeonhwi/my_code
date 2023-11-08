<template>
    <div>
        <h1>부모 페이지입니다.</h1>
        <ChildPage :my-msgs="children" @change-balance="changeBalance" />
    </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from '@/components/ChildPage.vue'

const children = ref([
    {name:'김하나', age:30, balance:100000},
    {name:'김두리', age:20, balance:10000},
    {name:'김서이', age:10, balance:1000},
])

const changeBalance = function (index) {
    children.value[index].balance += 1000
}

</script>

<style scoped>
div {
    border: solid 0.5px rgb(177, 171, 171);
    padding: 4px;
    margin: 8px;
}
</style>