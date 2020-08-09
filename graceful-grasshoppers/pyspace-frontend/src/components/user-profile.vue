<template>
  <div class="profile-box" style="flex: 0 1 400px;">
    <h1>{{ user.username }}</h1>
    <div class="details-box flex-row">
      <span class="profile-picture">
        <img width="150" v-bind:src="baseURL+'/media/'+user.profile_picture">
      </span>
      <div class="flex-col">
       <span class="age">{{ user.age }} years old</span>
       <span class="gender">{{ user.gender }}</span>
       <span class="country">{{ user.country }}</span>       
     </div>
   </div>
   <div v-if="logged_in" class="contact-user bordered">
    <span class="flex-row p-0">
      <ul class="p-0 w-50">
        <li v-on:click="follow" class="p-0 m-0"><button href="#">Add as friend</button></li>
      </ul>
    </span>
   </div>
   <div class="pyspace-url bordered">
    <p class="font-weight-bold m-0">PySpace Url :</p>
    <a href="#">https://pyspace.net/?id={{ user.id }}</a>
   </div>
 </div>
</template>

<script>
// @ is an alias to /src
import axios from '../http-common.js';
import authHeader from '@/services/auth-header.js';
export default {
  name: 'UserProfile',
  props: ['user', 'logged_in'],
  data: function() {
    return {
      baseURL: axios.defaults.baseURL,
    }
  },
  methods: {
    follow() {
      axios
      .post('/befriend/?username='+user.username)
      .then((response) => {
        this.$router.push('/friends');
      })
    }
  }
};

</script>
