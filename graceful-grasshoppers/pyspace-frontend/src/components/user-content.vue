<template>
  <div class="profile-box flex-col" style="flex: 0 1 600px;">
    <UserAbout />
    <UserFriends />
    <UserComments />
 </div>
</template>

<script>
import UserFriends from '@/components/user-friends';
import UserComments from '@/components/user-comments';
import UserAbout from '@/components/user-about';
export default {
  name: 'UserContent',
  components: {
    UserFriends,
    UserComments,
    UserAbout,
  }
}
</script>

<style>
</style>