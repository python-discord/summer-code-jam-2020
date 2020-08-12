export class Identity { }

Identity.create = function (name) {
  return new roles[name]()
}

class Role extends Identity { }

export class Anonymous extends Role { }

class Reader extends Anonymous { }

class Author extends Reader { }

class Editor extends Author { }

class Moderator extends Author { }

class Admin extends Moderator { }

export class IAM {
  constructor (store) {
    this.store = store
    this.identity = null
  }

  needs (roleName) {
    const role = roles[roleName]
    return this.store.getters.identity instanceof role
  }
}

const roles = {
  Anonymous,
  Reader,
  Author,
  Editor,
  Moderator,
  Admin
}

export default {
  install (Vue, { store }) {
    console.log('Installing IAM plugin')
    Vue.prototype.$iam = new IAM(store)
  }
}
