<template>
    <div>
        <br>
        <h4>이름 : {{ myMsg.name }}</h4>
        <p>직함 : {{ myMsg.title }}</p>
        <button @click="deleteCardEvent">명함 삭제</button>
    </div>
</template>

<script setup>
const emit = defineEmits (['delete'])
const deleteCardEvent = function() {
    emit('delete')
}


defineProps ({
    myMsg: Object,
})
</script>

<style scoped>
div {
    width: 300px;
    height: 150px;
    display: block;
    /* flex-direction: column; */
    align-items: center;
    /* justify-content: center; */
    padding: 15px;
    background-color: rgb(247, 247, 243);
    border: solid 1px gray;
    margin: 10px;
}
</style>