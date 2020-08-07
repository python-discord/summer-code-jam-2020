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
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
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
    path: "/profile/:id",
    name: "Profile",
    component: () => import("../views/Profile.vue"),
  },
  {
    path: "/create-post",
    name: "CreatePost",
    component: () => import("../views/CreatePost.vue")
  },
  {
    path: "/friends",
    name: "Friends",
    component: () => import("../views/Friends.vue")
  },
  {
    path: "/posts",
    name: "Posts",
    component: () => import("../views/Posts.vue")
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
