<template>
    <div>
        <h1>가수 목록</h1>
        <template v-for="singer in singers">
            <SingerDetail/>
        </template>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import SingerDetail from '@/components/singers/SingerDetail.vue';
const singers = ref([
    {name:'adele'},
    {name:'maroon 5'},
    {name:'Dua'}
])
</script>

<style scoped>
div {
    text-align: center;
}
h1 {
    color: orangered;
}
</style>