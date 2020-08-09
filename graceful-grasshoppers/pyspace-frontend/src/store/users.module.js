import UserService from "../services/user.service";

/*
const user = JSON.parse(localStorage.getItem("user"));
const initialState = user
  ? { status: { loggedIn: true }, user }
  : { status: { loggedIn: false }, user: null };
  */

export const users = {
  namespaced: true,
  state: {user:null},
  actions: {
    getLoggedInUserProfile({ commit }) {
      return UserService.getLoggedInUserProfile().then(
        (user) => {
          commit("getLoggedInUserProfileSuccess", user);
          return Promise.resolve(user);
        },
        (error) => {
          commit("getLoggedInUserProfileFailure");
          return Promise.reject(error);
        }
      );
    },
    /*
    logout({ commit }) {
      AuthService.logout();
      commit("logout");
    },
    */
  },
  mutations: {
    getLoggedInUserProfileSuccess(state, user) {
      state.status.loggedIn = true;
      state.user = user;
    },
    getLoggedInUserProfileFailure(state) {
      state.status.loggedIn = false;
      state.user = null;
    },
  },
};
