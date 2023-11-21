<template>
    <div>
        <p @click="goToMyPage(props.mypageToLike)">유저 : {{ props.mypageToLike }}</p>
    </div>
</template>

<script setup>
import { useRouter} from 'vue-router'

const router = useRouter()

const props = defineProps({
    mypageToLike:Number,
})

const goToMyPage = function(userId) {
    console.log('안녕')
    const absolutePath = `/mypage/${userId}`
    router.push(absolutePath)

    // 일정 시간(예: 100ms)을 기다린 후에 리로드 실행 router.push는 비동기이기 때문
    setTimeout(() => {
        location.reload();
    }, 100);
}

</script>

<style scoped>

</style>