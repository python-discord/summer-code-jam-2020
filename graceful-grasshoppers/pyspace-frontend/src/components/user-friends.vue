<template>
<div class="user-friends flex-col w-75">
    <h1>Friends</h1>
    <p v-if="loggedInUser" class="alert-info font-weight-bold">Your friends</p>
    <p v-else class="alert-info font-weight-bold">{{ user.username }}'s friends</p>
    <h6 v-if="loggedInUser">You have {{ user.friends.length }} friend(s)!</h6>
    <h6 v-else>{{ user.username }} has {{ user.friends.length }} friends!</h6>
    <div class="friend" style="width: 100px;" v-for="friend in user.friends" :key="friend.id">
        <img src="http://placehold.it/100x100">
        <a v-bind:href="'/profile/'+friend.username">{{ friend.username }}</a>
    </div>
</div>
</template>
<script>
export default {
    name: 'UserFriends',
    props: ['loggedInUser', 'user'],
};
</script>