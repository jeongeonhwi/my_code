<template>
    <div>
        <h1>학생 상세 정보 목록 입니다.</h1>
        <p v-for="student in studentInfo">이름 : {{ student.name }}
            <span @click="goToDetail(student.name)">
                정보 보기
            </span>
        </p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import router from '../router';

const studentInfo = ref([
    {name:'김하나'},
    {name:'김두리'},
    {name:'김서이'},
])

const goToDetail = function(studentName) {
    // console.log(studentName)
    router.push({ name:'studentdetail', params: {name: studentName} })
}
</script>

<style scoped>

</style>