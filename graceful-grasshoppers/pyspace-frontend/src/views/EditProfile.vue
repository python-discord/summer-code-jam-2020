<template>
  <div class="container mt-5 mb-5 flex-col">
    <form @submit.prevent="onSubmit" class="flex-col">
      <label for="about">About</label>
      <textarea id="about" v-model="user.about"></textarea>
      <label for="age">Age</label>
      <input id="age" placeholder="" type="number" v-model="user.age">
      <label for="picture">Profile Picture</label>
      <input type="file" ref="image" name="">
      <input type="submit" value="Update Profile">
    </form>
  </div>
</template>

<script>
  import UserProfile from '@/components/user-profile';
  import UserContent from '@/components/user-content';
  import User from '@/models/user';
  import axios from '../http-common.js';
  import authHeader from '@/services/auth-header';

  export default {
    name: 'Profile',
    data: function() {
      return {
        user: new User({}),
      }
    },
    methods: {
      init() {
        axios
        .get('/users/self/', { headers: authHeader() })
        .then((response) => { Object.assign(this.user, response.data); console.log(response) })
      },
      onSubmit() {
        let data = new FormData();

        data.append('profile_picture', this.$refs.image.files[0]);
        data.append('about', this.user.about);
        data.append('age', this.user.age);

        axios
        .patch('/users/update/',
          data,
          {
            headers: {
              'content-type': 'multipart/form-data',
              'Authorization': authHeader().Authorization,
            }
          })
        .then(() => {
          this.$router.push('/profile');
        })
      },
      uploadProfilePic(event) {
        const formData = new FormData();
        const image = event.target.files[0];
        formData.append("image", image);
        console.log(formData)
        axios
        .post('/upload/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: authHeader().Authorization,
          }
        })
        .then((response) => {
          this.$router.push('/profile');
        })
      }
    },
    mounted() {
      this.init();
    },
  }
</script>

<style>
</style>