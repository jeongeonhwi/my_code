<template>
    <div class="card">
        <h1>가수 이름</h1>
        <img src="@/assets/singer.jpg" alt="singer">
        <p>가수 소개글</p>
        <div class="album">
            <SingerAlbum/>
            <SingerAlbum/>
        </div>
        <br>
    </div>
</template>

<script setup>
import SingerAlbum from '@/components/singers/SingerAlbum.vue';
</script>

<style scoped>
img {
    width: 200px;
    border-radius: 50%;
}
.card {
    border: solid black 1px;
    display: inline-block;
    text-align: center;
    width: 40%;
    margin: 20px;
    /* grid-template-rows: max-content 200px 1fr; */
}
.album {
    display: flex;
    justify-content: center;
}
</style>