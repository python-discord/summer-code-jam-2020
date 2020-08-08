<template>
  <div class="profile-box flex-col" style="flex: 0 1 600px;">
    <UserAbout v-bind:user="user" />
    <UserFriends v-bind:user="user" />
    <UserComments v-bind:user="user" />
 </div>
</template>

<script>
import UserFriends from '@/components/user-friends';
import UserComments from '@/components/user-comments';
import UserAbout from '@/components/user-about';
export default {
  name: 'UserContent',
  props: ['user'],
  components: {
    UserFriends,
    UserComments,
    UserAbout,
  },
}
</script>

<style>
</style>