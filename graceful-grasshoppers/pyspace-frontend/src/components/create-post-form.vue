<template>
    <div>
        <form class="flex-col" @submit.prevent="onSubmit">
            <label for='title'>Title</label>
            <input v-model="post.title" id='title' type="" name="">
            <label for='content'>Content</label>
            <textarea v-model="post.content" id="content"></textarea>
            <input @change="print" value="Add a post image" type="file" name="">
            <input type="submit" value="Post">
        </form>
    </div>
</template>

<script type="text/javascript">
import Post from '../models/post';
import axios from '../http-common.js';
import authHeader from '@/services/auth-header';

export default {
    name: 'CreatePostForm',
    data() {
        return {
            post: new Post({}),
        };
    },
    methods: {
        onSubmit() {
            axios
            .post('/posts/create/',
            {
                title: this.post.title,
                content: this.post.content,
            },
            {
                headers: authHeader(),
            })
            .then((response) => {
                if (response.status == 201) this.$router.push('/posts');
            })
        },
        print: {
            getImageData(event) {
                let selectedFile = event.target.files[0];
                let formData = new FormData();
                formData.append("fileToUpload", selectedFile);
                console.log(formData);
            }
        }
    }
}
</script>

<style>
.flex-col {
    display: flex;
    flex-direction: column;
}

label {
    text-align: left;
}
</style>