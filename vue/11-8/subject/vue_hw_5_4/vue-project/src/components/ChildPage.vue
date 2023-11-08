<template>
    <div v-for="(myMsg , index) in myMsgs">
        <h3>자식 페이지입니다.</h3>
        <p>이름 : {{ myMsg.name }}</p>
        <p>나이 : {{ myMsg.age }}</p>
        <p>용돈 : {{ myMsg.balance }}</p>
        <p><button @click="giveMeMoney(index)">용돈 주세요.</button></p>
    </div>
</template>

<script setup>

defineProps(['myMsgs'])
const emit = defineEmits(['changeBalance'])
const giveMeMoney = function (index) {
    emit('changeBalance', index)
}
</script>

<style scoped>
div {
    border: solid 0.5px rgb(185, 178, 178);
    margin: 8px;
    padding: 8px;
}

</style>