<template>
<div class="user-friends flex-col w-75">
    <h1>Friends</h1>
    <p v-if="loggedInUser" class="alert-info font-weight-bold">Your friends</p>
    <p v-else class="alert-info font-weight-bold">{{ user.name }}'s friends</p>
    <h6 v-if="loggedInUser">You have {{ user.friends.length }} friends!</h6>
    <h6 v-else>{{ user.name }} has {{ user.friends.length }} friends!</h6>
    <div class="friend" v-for="friend in user.friends" :key="friend.id">
        <img src="http://placehold.it/100x100">
        <a v-bind:href="'#'">{{ friend.name }}</a>
    </div>
</div>
</template>
<script>
// @ is an alias to /src
// import axios from "../http-common";
import axios from "axios";
import User from "../models/user";
// const authToken = JSON.parse(localStorage.getItem('user')).key;
export default {
    name: 'UserFriends',
    props: ['user', 'userPicture', 'url', 'title', 'artist'],
    data: function() {
        return {
            user: this.user,
            userPicture = this.userPicture,
            url: this.url,
            title: this.title,
            artist: this.artist,
        };
    },
};
</script>