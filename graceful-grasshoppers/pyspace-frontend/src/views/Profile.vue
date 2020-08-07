<template>
  <div class="container mt-5 mb-5" style="display: flex;">
    <UserProfile />
    <UserContent />
  </div>
</template>

<script>
import UserProfile from '@/components/user-profile';
import UserContent from '@/components/user-content';
export default {
  name: 'Profile',
  components: {
    UserProfile,
    UserContent,
  }
}
</script>

<style>
</style>