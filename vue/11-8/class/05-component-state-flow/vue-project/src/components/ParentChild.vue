<template>
    <div>
        {{ myMsg }}
        <ParentGrandChild @update-name="updateName" :my-msg="myMsg" />
        <p>
        {{ dynamicProps }}
        </p>
        <button @click="$emit('someEvent')">클릭</button>
    </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'

// 객체 선언 방식
defineProps({
    myMsg: String,
    dynamicProps: String,
    }
)
const emit = defineEmits(['updateName'])
const updateName = function () {
    emit('updateName')
}
</script>

<style scoped>

</style>