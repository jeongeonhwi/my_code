<template>
    <div>
        <h1>가수 목록</h1>
        <SingerDetail/>
        <SingerDetail/>
    </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue';
</script>

<style scoped>
div {
    text-align: center;
}
h1 {
    color: orangered;
}
</style>