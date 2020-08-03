class KeyboardNavigator {
  constructor(router) {
    this.router = router;
    this.watchers = this.getDefaultWatchers();
    this.unkownCommand = undefined;
  }

  getDefaultWatchers() {
    const defaultCommands = {
      '/home': [() => this.router.push('/')],
    };
    return defaultCommands;
  }

  on(commandName, callback) {
    if (this.watchers[commandName] === undefined) {
      this.watchers[commandName] = [];
    }
    this.watchers[commandName].push(callback);
  }

  onUnknown(callback) {
    this.unkownCommand = callback;
  }

  emitCommand(command) {
    if (this.watchers[command] !== undefined) {
      for (let i = 0; i < this.watchers[command].length; i++) {
        this.watchers[command][i]();
      }
    } else if (this.unkownCommand !== undefined) {
      this.unkownCommand(command);
    }
  }

  reset() {
    this.watchers = this.getDefaultWatchers();
  }
}

export default {
  install(vue, { router }) {
    const prompter = new KeyboardNavigator(router);
    vue.prototype.$cmd = prompter; // eslint-disable-line no-param-reassign
  },
};
