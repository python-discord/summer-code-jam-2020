<template>
  <div class="container">
    <h3 style="text-align: center;">Login</h3>
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from '@/components/login-form';
export default {
    name: 'Login',
    components: {
        LoginForm
    }
}
</script>

<style>
</style>