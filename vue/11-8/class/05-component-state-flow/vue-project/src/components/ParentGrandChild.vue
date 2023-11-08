<template>
    <div>
        {{ myMsg }}
        <button @click="updateName">이름변경</button>
    </div>
</template>

<script setup>
const emit = defineEmits(['updateName'])
const updateName = function () {
    emit('updateName')
}

defineProps({
    myMsg:String
})
</script>

<style scoped>

</style>