<template>
    <div>
        <ParentChild @update-name="updateName" @some-event="someCallback" my-msg="message" :dynamic-props="name"/>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import ParentChild from '@/components/ParentChild.vue';

const name = ref('Alice')

const someCallback = function () {
    console.log('Parentchild가 발신한 이벤트를 수신했어요')
}

const updateName = function () {
    name.value = 'Bella'
}
</script>

<style scoped>

</style>