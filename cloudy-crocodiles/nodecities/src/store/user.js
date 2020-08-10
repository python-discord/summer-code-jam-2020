import jwtDecode from 'jwt-decode'
import gql from 'graphql-tag'
import { Identity, Anonymous } from '../iam'
import { $apolloClient } from '../apollo/apollo-client-hooks'

const directives = process.env.STANDALONE ? '@client' : ''

const state = {
  authStatus: '',
  authToken: null,
  user: null,
  identity: new Anonymous()
}

const getters = {
  authStatus: (state) => {
    return state.authStatus
  },
  isLoggedIn: (state) => {
    /*
    if (localStorage.getItem('user') !== null) {
      state.authStatus = 'success'
    } */
    return state.authStatus === 'success'
  },
  authToken: (state) => {
    return state.authToken
  },
  user: (state) => {
    return state.user
  },
  identity: (state) => {
    return state.identity
  }
}

const actions = {
  login: (info, data) => {
    const { commit, rootState } = info
    console.log(info)
    // commit('login') // show spinner
    return new Promise((resolve, reject) => {
      $apolloClient.mutate({
        // Query
        mutation: gql`
          mutation ($data: LoginInput!) {
            login(data: $data) ${directives} {
              token
            }
          }`,
        // Parameters
        variables: {
          data
        }
      }).then((data) => {
        console.log('login success')
        console.log(data)
        commit('loginSuccess', data.data.login)
        resolve()
      }).catch((err) => {
        reject(err.message);
      })
    })
  },
  logout: ({ commit }) => {
    commit('logout')
  },
  getLocalStorageUser: ({ commit }) => {
    const token = localStorage.getItem('user-token');
    if (token === null) return null;
    commit('loginSuccess', { token });
  },
}

const mutations = {
  login: (state) => {
    state.authStatus = 'pending'
  },
  loginSuccess: (state, data) => {
    console.log('login success')
    if (process.env.STANDALONE) {
      state.authStatus = 'success'
      return
    }
    const token = data.token
    state.authToken = token
    localStorage.setItem('user-token', token)
    console.log('Token', token)

    const user = jwtDecode(token)
    state.user = user
    localStorage.setItem('user', user)
    console.log('User', user)

    // TODO: Fix this!!!
    // state.identity = Identity.create(user.role)
    state.identity = Identity.create('Admin')

    state.authStatus = 'success'
  },
  logout: (state) => {
    console.log('logout')
    state.authStatus = ''
    state.authToken = null
    state.user = null
    localStorage.removeItem('user')
    localStorage.removeItem('user-token')
  }
}
export default {
  state,
  getters,
  mutations,
  actions
}
