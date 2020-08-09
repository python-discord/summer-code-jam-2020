<template>
  <q-page padding>
    <div class="card-column">
      <q-card v-for="site in citySites" :key="site.id">
        <q-card-section>
          <a :href="`http://localhost:1234/${city.slug}/${site.address}/index.html`">
            {{ `${city.name}/${site.address}` }}
          </a>
          <br/>
          <a :href="`/sites/${site.id}`">
            Edit
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
    id,
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
