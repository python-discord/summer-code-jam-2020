class KeyboardNavigator {
  constructor(router, store) {
    this.router = router;
    this.watchers = this.getDefaultWatchers();
    this.unkownCommand = undefined;
    this.defaultUnknown = undefined;
    this.inputCallback = undefined;
    this.clearText = undefined;
    this.textRelayInProgress = false;
    this.store = store;
    this.store.commit('setInstructions', []);
  }

  init(onUnknown, askForInput, clearText) {
    this.unkownCommand = onUnknown;
    this.defaultUnknown = onUnknown;
    this.inputCallback = askForInput;
    this.clearText = clearText;
  }

  getDefaultWatchers() {
    const defaultCommands = {
      '/home': [() => this.router.push('/')],
      '/logout': [() => this.router.push('/logout')],
    };
    return defaultCommands;
  }

  input(prompter, hidden) {
    this.textRelayInProgress = true;
    return this.inputCallback(prompter, hidden);
  }

  on(commandName, callback, instructions) {
    if (this.watchers[commandName] === undefined) {
      this.watchers[commandName] = [];
    }
    this.watchers[commandName].push(callback);
    if (instructions) {
      this.store.commit('addInstructions', {
        cmd: commandName,
        help: instructions,
      });
    }
  }

  onUnknown(callback) {
    this.unkownCommand = callback;
    return this.defaultUnknown;
  }

  addDefaultUnknown(callback) {
    this.defaultUnknown = callback;
  }

  emitCommand(command) {
    if (this.watchers[command] !== undefined) {
      this.watchers[command].map((x) => x());
    } else if (this.unkownCommand !== undefined) {
      if (!this.textRelayInProgress) {
        this.unkownCommand(command);
      }
    }
    this.clearText();
  }

  reset() {
    this.watchers = this.getDefaultWatchers();
    this.unkownCommand = this.defaultUnknown;
    this.textRelayInProgress = false;
    this.store.commit('setInstructions', []);
    this.clearText();
  }
}

export default {
  install(vue, { router, store }) {
    const prompter = new KeyboardNavigator(router, store);
    vue.prototype.$cmd = prompter; // eslint-disable-line no-param-reassign
  },
};
