<template>
  <div id="bbs-input-container" @click="focusInput">
    <div class="output-field" v-if="output">
      {{output}}
    </div>
    <div id="bbs-input-form">
      {{promptMessage}}<input ref="cmdinput"
      v-model="value"
      id="bbs-input-field"
      @keyup.enter="execCommand"
      :type="hidden ? 'password' : 'text'"
      autofocus>
    </div>
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
  padding: unset;
  font-size: unset;
}
</style>

<script>
export default {
  data() {
    return {
      value: '',
      output: '',
      currentPrompt: '',
      askingForMessage: false,
      promptResolver: null,
      hidden: false,
    };
  },
  computed: {
    username() {
      return this.$store.state.username || 'guest';
    },
    promptMessage() {
      if (this.askingForMessage) {
        return this.currentPrompt || '> ';
      }
      return `${this.username}@llamma$ `;
    },
  },
  beforeMount() {
    this.$cmd.init(this.raiseUnknown, this.askForInput, this.clearText);
  },
  methods: {
    askForInput(prompter, hidden) {
      this.askingForMessage = true;
      this.hidden = hidden || false;
      this.currentPrompt = prompter;
      return new Promise((resolve) => {
        this.promptResolver = resolve;
      });
    },
    focusInput() {
      this.$refs.cmdinput.focus();
    },
    raiseUnknown(command) {
      this.output = `Error: Invalid command ${command}`;
    },
    execCommand() {
      if (this.promptResolver) {
        this.promptResolver(this.value);
        this.promptResolver = null;
        this.currentPrompt = '';
        this.askingForMessage = false;
        this.hidden = false;
      }
      this.output = '';
      this.$cmd.emitCommand(this.value);
      this.clearText();
    },
    clearText() {
      this.value = '';
    },
  },
};
</script>
