import { defineStore } from "pinia";
import { ref, computed } from "vue";
import axios from 'axios'


export const usePostStore = defineStore('posts', () => {
    // state
    const postList = ref([])
    const categoryList = ref([])

    // getters
    const postListValue = computed(() => {
        return postList.value
    })
    const categoryListValue = computed(() => {
        return categoryList.value
    })
    // actions
    const getPostList = () => {
        axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/api/v1/posts/'
        })
            .then((res) => {
                // console.log(res.data)
                postList.value = res.data
            })
            .catch((error) => {
                console.log(error)
            })
    }
    const getCategoryList = () => {
        axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/api/v1/category/'
        })
            .then((res) => {
                // console.log(res.data)
                categoryList.value = res.data
            })
            .catch((error) => {
                console.log(error)
            })
    }
    return {
        postListValue,
        getPostList,
        categoryListValue,
        getCategoryList,
    }
})