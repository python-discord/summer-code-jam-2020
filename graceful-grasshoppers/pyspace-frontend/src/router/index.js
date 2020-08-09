import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import { BootstrapVue } from "bootstrap-vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(VueRouter);
Vue.use(BootstrapVue);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("../views/Register.vue"),
  },
  {
    path: "/profile/:id?",
    name: "Profile",
    component: () => import("../views/Profile.vue"),
  },
  {
    path: "/create-post",
    name: "CreatePost",
    component: () => import("../views/CreatePost.vue")
  },
  {
    path: "/friends/:userId?",
    name: "Friends",
    component: () => import("../views/Friends.vue")
  },
  {
    path: "/posts/:userId?",
    name: "Posts",
    component: () => import("../views/Posts.vue")
  },
  {
    path: "/post/:postId",
    name: "Post",
    component: () => import("../views/Post.vue")
  },
  {
    path: "/editprofile",
    name: "EditProfile",
    component: () => import("../views/EditProfile.vue")
  },
  {
    path: "/random",
    name: "Random",
    component: () => import("../views/Random.vue")
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
