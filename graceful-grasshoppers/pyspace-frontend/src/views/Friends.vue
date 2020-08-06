<template>
  <div class="home mt-5" style="margin: auto;">
    <FriendsList logged-in-user='false'/>
  </div>
</template>

<script>
// @ is an alias to /src
import FriendsList from '@/components/user-friends';

export default {
  name: 'Friends',
  components: {
  	FriendsList,
  }
}
</script>
