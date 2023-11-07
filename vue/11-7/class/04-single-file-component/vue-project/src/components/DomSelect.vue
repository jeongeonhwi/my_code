<template>
    <div>
        <input type="text" ref="ssafy">
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const ssafy = ref()

onMounted(() => {
    console.log(ssafy.value)
})
</script>

<style scoped>

</style>