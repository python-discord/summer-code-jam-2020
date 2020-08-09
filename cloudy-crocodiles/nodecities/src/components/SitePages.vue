<template>
  <q-page padding>
    <q-list v-if="site">
      <q-item v-for="page in site.pages" :key="page.id">
        <q-item-section avatar>
          <q-btn flat icon="edit" :to="`/pages/${page.id}/edit`" />
        </q-item-section>
        <q-item-section>
          <a :href="`/pages/${page.id}`">
            {{ page.file_name }}
          </a>
        </q-item-section>
      </q-item>
    </q-list>
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
      <q-btn fab icon="add" color="accent" to="/pages/add" />
    </q-page-sticky>
  </q-page>
</template>

<script>
export default {
  name: 'SitePages',
  props: ['site'],
  data() {
    return {
    };
  },
  methods: {
  },

};
</script>
