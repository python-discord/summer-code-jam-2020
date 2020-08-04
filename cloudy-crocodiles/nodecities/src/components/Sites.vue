<template>
  <q-page padding>
    <div class="card-column">
      <q-card v-for="site in allSites" :key="site.slug">
        <q-card-section>
          <a :href="`/sites/${site.slug}`">
            {{ city.name + site.address }}
          </a>
        </q-card-section>
        <q-card-section>
          {{ site.description }}
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import gql from 'graphql-tag';

const sitesQuery = gql`
query sitesQuery {
  allSites {
    address,
    description
  }
}
`;

export default {
  name: 'Sites',
  props: ['city'],
  data() {
    return {
    };
  },
  apollo: {
    allSites: {
      query: sitesQuery,
      prefetch: false,
      fetchPolicy: 'network-only',
    },
  },
  methods: {
  },

};
</script>
