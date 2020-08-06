<template>
    <div>
        <form class="flex-col" @submit.prevent="onSubmit">
            <label for='title'>Title</label>
            <input id='title' type="" name="">
            <label for='content'>Content</label>
            <textarea id="content"></textarea>
            <input @change="print" value="Add a post image" type="file" name="">
            <input type="submit" value="Post">
        </form>
    </div>
</template>

<script type="text/javascript">
import Post from '../models/post';
export default {
    name: 'CreatePostForm',
    data() {
        return {
            post: new Post(),
            message: '',
        };
    },
    methods: {
        onSubmit() {
            console.log(this.post.image);
        },
        print: getImageData(event) {
            let selectedFile = event.target.files[0];
            let formData = new FormData();
            formData.append("fileToUpload", blobFile);
            console.log(formData);
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