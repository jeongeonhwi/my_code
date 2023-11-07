<template>
    <div class="card">
        <h1>가수 이름</h1>
        <img src="@/assets/singer.jpg" alt="singer">
        <p>가수 소개글</p>
    </div>
</template>

<script setup>

</script>

<style scoped>
img {
    width: 200px;
    border-radius: 50%;
}
div {
    border: solid black 1px;
}
.card {
    display: inline-block;
    text-align: center;
    width: 40%;
    margin: 20px;
    /* grid-template-rows: max-content 200px 1fr; */
}
</style>