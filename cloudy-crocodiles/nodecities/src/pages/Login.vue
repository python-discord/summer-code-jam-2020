<template>
  <q-page padding>
    <form @submit.prevent="handleSubmit">
        <q-input autocomplete="username" v-model="username" type="username" label="Username" />
        <q-input autocomplete="current-password" v-model="password" type="password" label="Password" />
        <q-btn flat color="primary" type="submit" label="Submit" />
    </form>
  </q-page>
</template>

<style>
</style>

<script>
import { UserMixin } from 'src/mixins'

export default {
  name: 'LoginPage',
  mixins: [UserMixin],
  props: ['isLogout'],
  data () {
    return {
      title: 'Login',
      username: '',
      password: ''
    }
  },
  mounted () {
    if (this.isLogout) {
      this.$store.dispatch('logout')
    }
  },
  methods: {
    handleSubmit () {
      this.$store.dispatch('login', {
        username: this.username,
        password: this.password
      }).then(() => {
        this.$router.push('/')
      }).catch((err) => {
        console.log(err)
        console.log('bad login')
      })
    }
  }
}
</script>
