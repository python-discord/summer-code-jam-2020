<template>
  <q-page padding>
    <q-list v-if="site">
      <q-item v-for="page in site.pages" :key="page.id">
        <q-item-section>
          <a :href="`/pages/${page.id}`">
            {{ page.file_name }}
          </a>
        </q-item-section>
      </q-item>
    </q-list>
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
