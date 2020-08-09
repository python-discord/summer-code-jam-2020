<template>
  <div v-if="ready">
    <h2>Forum</h2>
    <ol class="home-menu-options">
      <li v-for="item in myStuff">
        <router-link :to="{ name: 'thread-view', params: {id:item.id}}">{{ item.title }} - Posted:
          {{ item.created_date | moment("DD.MM.YY, hh:mm")  }} by {{item.created_by_id}}
        </router-link>
      </li>
    </ol>
  </div>
</template>

<style>
.some-heading {
  font-size: xx-large;
  color: pink;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      myStuff: [],
      ready: false,
      errorCallback: undefined,
    };
  },
  beforeMount() {
    this.getData();
  },
  mounted() {
    this.errorCallback = this.$cmd.onUnknown(this.enterThread);
    this.$cmd.on('/open <number>', () => undefined, 'Read thread <number>');
    this.$cmd.on('/new', () => this.$router.push('/forum/new'), 'Open a new thread');
  },
  methods: {
    enterThread(command) {
      if (command.startsWith('/open ')) {
        const cmd = command.split(' ')[1];
        if (isNaN(cmd)) {
          this.errorCallback(command);
        } else {
          this.goToThread(Number(cmd) - 1);
        }
      } else {
        this.errorCallback(command);
      }
    },
    goToThread(threadIndex) {
      this.$router.push({
        name: 'thread-view',
        params: {
          id: this.myStuff[threadIndex].id,
        },
      });
    },
    getData() {
      axios.get('/api/forum/').then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },
  },
};
</script>
