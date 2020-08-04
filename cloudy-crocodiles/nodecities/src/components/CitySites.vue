<template>
  <q-page padding>
    <div>
      <q-card v-for="site in citySites" :key="site.id">
        <q-card-section>
          <!-- <a :href="`/sites/${site.id}`"> -->
          <a :href="`http://localhost:1234/${city.slug}/${site.address}`">
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
query sitesQuery($id: ID!) {
  citySites(id: $id) {
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
    citySites: {
      query: sitesQuery,
      prefetch: false,
      fetchPolicy: 'network-only',
      variables () {
        return {
          id: this.city.id
        }
      },
    },
  },
  methods: {
  },

};
</script>
