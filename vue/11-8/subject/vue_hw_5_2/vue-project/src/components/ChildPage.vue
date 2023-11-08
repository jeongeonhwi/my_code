<template>
    <div v-for="myMsg in myMsgs">
        <h3>자식 페이지입니다.</h3>
        <p>이름:{{ myMsg.name }}</p>
        <p>나이:{{ myMsg.age }}</p>
    </div>
</template>

<script setup>
defineProps(['myMsgs'])
</script>

<style scoped>
div {
    border: solid 0.5px rgb(185, 178, 178);
    margin: 8px;
    padding: 8px;
}

</style>