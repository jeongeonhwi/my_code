<template>
    <div>
        <h4>리뷰컴포넌트</h4>
        {{ props.movieToReview.score }} | {{ props.movieToReview.content }}
    </div>
</template>

<script setup>
const props = defineProps({
    movieToReview:Object,
})
</script>

<style scoped>

</style>