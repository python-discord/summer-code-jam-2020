<template>
  <div class="instructions-panel" v-if="notLogin">
    <h2>Help</h2>
    <div class="instruction-set" v-for="command in fullCommands">
      <span class="command">{{command.cmd}}</span>
      <span v-if="command.help" class="command-help">{{command.help}}</span>
    </div>
  </div>
</template>

<style>
#content {
  display: grid;
  grid-template-columns: 1fr 5fr 2fr;
}
.instructions-panel {
  margin-left: 1em;
  border-left: 2px solid var(--font-color);
  padding-left: 1em;
}

.instruction-set {
  font-size: 12pt;
}
.instruction-set .command {
  font-weight: bolder;
  font-size: 14pt;
}
</style>

<script>
const DEFAULT_COMMANDS = [
  { cmd: '/home' },
  { cmd: '/logout' },
];
export default {
  data() {
    return {
      commands: DEFAULT_COMMANDS,
    };
  },
  computed: {
    routeName() {
      return this.$route.name;
    },
    notLogin() {
      return !(this.routeName === 'login_page' || this.routeName === 'logout_page');
    },
    storedInstructions() {
      return this.$store.state.instructions;
    },
    fullCommands() {
      return this.commands.concat(this.storedInstructions);
    },
  },
};
</script>
