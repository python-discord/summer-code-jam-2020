<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          DjangoCities
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
        <q-expansion-item
          v-if="user !== null"
          icon="account_circle"
          :label="user.sub"
          v-model="userExpanded"
          expand-separator
        >
          <q-item
            clickable
            :to="{ name: 'userOwnSites'}"
          >
            <q-item-section avatar>
              <q-icon name="account_tree" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Your sites</q-item-label>
            </q-item-section>
          </q-item>
          <q-item
            clickable
            @click="handleLogout"
          >
            <q-item-section avatar>
              <q-icon name="lock" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Logout</q-item-label>
            </q-item-section>
          </q-item>
        </q-expansion-item>
        <EssentialLink
          v-else
          title="Login / Register"
          caption="Login"
          icon="login"
          link="/login"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue';

const linksData = [
  {
    title: 'Home',
    caption: 'Home',
    icon: 'home',
    link: '/',
  },
];

export default {
  name: 'MainLayout',
  components: { EssentialLink },
  data() {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData,
      userExpanded: true,
    };
  },
  computed: {
    user() {
      return this.$store.getters.user;
    },
  },
  methods: {
    handleLogout() {
      this.$store.dispatch('logout');
    },
  },
  created () {
    this.$store.dispatch('getLocalStorageUser');
  },
};
</script>
