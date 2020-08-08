class KeyboardNavigator {
  constructor(router) {
    this.router = router;
    this.watchers = this.getDefaultWatchers();
    this.unkownCommand = undefined;
    this.defaultUnknown = undefined;
    this.inputCallback = undefined;
    this.clearText = undefined;
    this.textRelayInProgress = false;
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
    };
    return defaultCommands;
  }

  input(prompter, hidden) {
    this.textRelayInProgress = true;
    return this.inputCallback(prompter, hidden);
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
    this.clearText();
  }
}

export default {
  install(vue, { router }) {
    const prompter = new KeyboardNavigator(router);
    vue.prototype.$cmd = prompter; // eslint-disable-line no-param-reassign
  },
};
