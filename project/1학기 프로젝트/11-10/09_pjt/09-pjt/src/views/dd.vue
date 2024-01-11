<template>
    <div class="modal" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p>Modal body text goes here.</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
            </div>
            </div>
        </div>
        </div>
    <div>
        <h1>유튜브 검색 및 출력 페이지</h1>
        <!-- {{ inputData }} -->
        <input type="text" placeholder="영화 제목을 입력하세요." 
        :value="inputData" 
        @input="onInput">
        <button
        @click="findMovie"
        >검색</button>
        <div v-for="youtube in youtubeList" class="box">
            <div @click="openModal">
                <p>{{youtube.snippet.title}}</p>
                <p>{{youtube.snippet.description}}</p>
                <img :src="youtube.snippet.thumbnails.default.url" alt=""> 
            </div>
        </div>
        
    </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const inputData = ref('')
const youtubeAPI = 'AIzaSyCuPsiJr84p9urvTlAVlPvAlaqeP-Aut7Y'
const youtubeList = ref('')

const onInput = function (event) {
    inputData.value = event.currentTarget.value
}

const findMovie = function () {
    const searchWord = inputData.value
    const youtubeURL = `https://www.googleapis.com/youtube/v3/search?key=${youtubeAPI}&part=snippet&type=video&q=${searchWord}`
    axios.get(youtubeURL)
        .then((response) => {
            youtubeList.value = response.data.items
        }).catch((error) => {
            console.log(error)
        })
}
</script>

<style scoped>
input {
    width: 50%;
    height: 30px;
}

.box {
    border: 1px solid black;
}
</style>