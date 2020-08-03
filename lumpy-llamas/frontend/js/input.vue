<template>
  <div id="bbs-input-container" @click="focusInput">
    <div class="output-field" v-if="output">
      {{output}}
    </div>
    <form @submit.prevent="execCommand" id="bbs-input-form">
      {{username}}@llamma$ <input ref="cmdinput" v-model="value" id="bbs-input-field" autofocus>
    </form>
  </div>
</template>

<style>
#bbs-input-container {
  border-top: 3px solid var(--font-color);
  width: 100%;
  position: fixed;
  bottom: 0;
  padding-top: 1em;
  margin-bottom: 1em;
}

#bbs-input-form {
  display: flex;
}

#bbs-input-field {
  border: none;
  margin-left: 0.5em;
  flex-grow: 3;
}
</style>

<script>
export default {
  data() {
    return {
      value: '',
      output: '',
    };
  },
  computed: {
    username() {
      return this.$store.state.username || 'guest';
    },
  },
  beforeMount() {
    this.$cmd.onUnknown(this.raiseUnknown);
  },
  methods: {
    focusInput() {
      this.$refs.cmdinput.focus();
    },
    raiseUnknown(command) {
      this.output = `Error: Invalid command ${command}`;
    },
    execCommand() {
      this.output = '';
      this.$cmd.emitCommand(this.value);
      this.value = '';
    },
  },
};
</script>
