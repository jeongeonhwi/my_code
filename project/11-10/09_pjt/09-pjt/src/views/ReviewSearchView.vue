<template>

    <div>
        <h1>유튜브 검색 및 출력 페이지</h1>
        <!-- {{ inputData }} -->
        <input type="text" placeholder="영화 제목을 입력하세요." 
        :value="inputData" 
        @input="onInput">
        <button
        @click="findMovie"
        >검색</button>
        <div v-for="youtube in youtubeList" :key="youtube.id.videoId" class="box">
            <div @click="openModal(youtube)" data-bs-toggle="modal" :data-bs-target="'#exampleModal'+youtube.id.videoId">
                <p>{{youtube.snippet.title}}</p>
                <p>{{youtube.snippet.description}}</p>
                <img :src="youtube.snippet.thumbnails.default.url" alt=""> 
                    <div class="modal fade" :id="'exampleModal'+youtube.id.videoId" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">{{youtube.snippet.title}}</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <iframe width="560" height="315" :src="'https://www.youtube.com/embed/'+ youtube.id.videoId" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
                                
                            </iframe>
                            
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Save changes</button>
                        </div>
                        </div>
                    </div>
                    </div>
            </div>
        </div>
        <!-- Button trigger modal -->
            <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Launch demo modal
            </button> -->

        <!-- Modal -->
    </div>
</template>



<script setup>
import { ref, reactive } from 'vue'
import axios from 'axios'
// import YoutubeIframeLoader from "youtube-iframe";

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
            // console.log(youtubeList.value[0].id.videoId)
        }).catch((error) => {
            console.log(error)
        })
}

const openModal = function () {
  // 부트스트랩 모달을 열기 위한 스크립트
  var myModal = new window.bootstrap.Modal(document.getElementById('myModal'));
  myModal.show();
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
